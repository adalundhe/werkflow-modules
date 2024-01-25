import asyncio
import functools
import re
from typing import Dict, Union, Optional
from concurrent.futures import ThreadPoolExecutor
from werkflow.modules.base import Module
from werkflow.modules.exceptions import MissingModuleError
from werkflow_encryption import Encryption
from werkflow_http import HTTP
from werkflow_http.connections.http.models.http import HTTPResponse
from werkflow.modules.system import System
from .exceptions import (
    BadRequestError,
    MethodNotAllowedError,
    ResourceNotFoundError,
    ServerFailedError,
    UnauthorizedRequestError,
    UnprocessableContentError
)
from .validators import (
    GithubRepoOptions,
    GithubBranchProtections,
    GithubPullRequest,
    GithubSecret,
    GithubVariable
)



class Github(Module):
    module_enabled=True
    dependencies=[
        'werkflow-http',
        'werkflow-encryption'
    ]

    def __init__(self) -> None:
        super().__init__()

        system = System()

        self._loop: asyncio.AbstractEventLoop = None
        self._executor = ThreadPoolExecutor(
            max_workers=system.configuration.cores.physical
        )

        self.client = HTTP()
        self.user: str = None

        self._errors_map = {
            (401, 403): UnauthorizedRequestError,
            (400, 400): BadRequestError,
            (404, 404): ResourceNotFoundError,
            (405, 405): MethodNotAllowedError,
            (422, 422): UnprocessableContentError,
            (500, 599): ServerFailedError
        }

        self._slug_pattern = re.compile(r'[^0-9a-zA-Z]+')
        self._duplicate_dash_pattern = re.compile(r'[-]+')
        self.project_slug: str = None
        self.encryption = Encryption()

    def check_response(self, response: HTTPResponse) -> HTTPResponse:
        if response.status < 200 or response.status >= 400:
            for error_code_range, error in self._errors_map.items():
                min_error_code, max_error_code = error_code_range

                if response.status >= min_error_code and response.status <= max_error_code:
                    raise error(
                        response.url,
                        response.method,
                        response.status
                    )
                
        return response

    async def slugify(
        self,
        project_name: str
    ) -> str:
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        project_slug = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._slug_pattern.sub,
                '-', 
                project_name
            )
        )

        project_slug = project_slug.lower().strip('-')
        
        return await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._duplicate_dash_pattern.sub,
                '-',
                project_slug
            )
        )
        

    async def login(
        self,
        access_token: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        response = await self.client.get(
            'https://api.github.com/octocat',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            }
        )
                
        return self.check_response(response)
    
    async def list_organization_repositories(
        self,
        organization: str,
        access_token: str,
        repos_per_page: int=100,
        page_number: int=1,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        response = await self.client.get(
            f'https://api.github.com/orgs/{organization}/repos?per_page={repos_per_page}&page={page_number}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            }
        )

        return self.check_response(response)
    
    async def get_repo(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'     
    ):
        response = await self.client.get(
            f'https://api.github.com/repos/{organization}/{project_name}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            }
        )

        return self.check_response(response)
        
    async def check_if_repo_exsits(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ):
        response = await self.client.get(
            f'https://api.github.com/repos/{organization}/{project_name}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            }
        )

        return response.status >= 200 and response.status < 300
    
    async def create_repo(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        description: str,
        team_id: Optional[str]=None,
        options: Dict[str, Union[bool, str]]={},
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)
        default_options = GithubRepoOptions(
            **{
                'name': project_slug,
                'description': description,
                'homepage': f'https://github.com/{organization}/{project_name}',
                'private': True,
                'has_issues': True,
                'has_projects': True,
                'has_wiki': True,
                'visibility': 'private',
                'team_id': team_id,
                **options
            }
        )

        parsed_options = default_options.json()

        response = await self.client.post(
            f'https://api.github.com/user/repos',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            },
            data=parsed_options
        )
    
        return self.check_response(response)
    
    async def create_organization_repo(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        description: str,
        team_id: Optional[str]=None,
        options: Dict[str, Union[bool, str]]={},
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)
        default_options = GithubRepoOptions(
            **{
                'name': project_slug,
                'description': description,
                'homepage': f'https://github.com/{organization}/{project_name}',
                'private': False,
                'has_issues': True,
                'has_projects': True,
                'has_wiki': True,
                'visibility': 'private',
                'team_id': team_id,
                **options
            }
        )

        parsed_options = default_options.json()

        response = await self.client.post(
            f'https://api.github.com/orgs/{organization}/repos',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-GitHub-Api-Version': f'{api_version}',
                'Accept': 'application/vnd.github+json'
            },
            data=parsed_options
        )
    
        return self.check_response(response)
    
    async def set_automated_security_fixes(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        enabled: bool=True,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        
        project_slug = await self.slugify(project_name)
        url = f'https://api.github.com/repos/{organization}/{project_slug}/automated-security-fixes'
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        if enabled:
            response = await self.client.put(
                url,
                headers=headers
            )
        
        else:
            response = await self.client.delete(
                url,
                headers=headers
            )

        return self.check_response(response)
        
    async def set_vulnerability_reports(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        enabled: bool=True,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        
        project_slug = await self.slugify(project_name)
        url = f'https://api.github.com/repos/{organization}/{project_slug}/vulnerability-alerts'
        
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        if enabled:
            response = await self.client.put(
                url,
                headers=headers
            )
        
        else:
            response = await self.client.delete(
                url,
                headers=headers
            )

        return self.check_response(response)
        
    async def set_branch_protections(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        branch_name: str='main',
        options: GithubBranchProtections={},
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        
        project_slug = await self.slugify(project_name)
        url = f'https://api.github.com/repos/{organization}/{project_slug}/branches/{branch_name}/protection'
    
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        protections = GithubBranchProtections(**{
            'required_status_checks': None,
            'enforce_admins': True,
            'required_pull_request_reviews': {
                'require_code_owner_reviews': False,
                'required_approving_review_count': 1,
                'require_last_push_approval': True,
                'dismiss_stale_reviews': True
            },
            'restrictions': None,
            'required_linear_history': False,
            'allow_force_pushes': False,
            'allow_deletions': False,
            'block_creations': False,
            'required_conversation_resolution': True,
            'lock_branch': False,
            'allow_fork_syncing': False,
            **options
        })

        parsed_options = protections.json(exclude_unset=True)

        response = await self.client.put(
            url,
            headers=headers,
            data=parsed_options
        )

        return self.check_response(response)
    
    async def get_repository_public_key(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/secrets/public-key'

        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def get_repository_secret(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        secret_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/secrets/{secret_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def list_repository_secrets(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/secrets'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def add_or_update_repository_secret(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        secret_name: str,
        secret_value: str,
        secret_already_encrypted: bool=False,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/secrets/{secret_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }
        
        response = await self.get_repository_public_key(
            access_token,
            project_name,
            organization=organization,
            api_version=api_version
        )

        public_key: Dict[str, str] = await response.json()
        key_id = public_key.get('key_id')

        key = public_key.get('key')
        self.encryption.key = key.encode()

        encrypted_secret = secret_value
        if secret_already_encrypted is False:

            if self.encryption.module_enabled is False:
                raise MissingModuleError(self.encryption)
        
            encrypted_secret = await self.encryption.encrypt_nacl(secret_value)

        github_secret = GithubSecret(
            key_id=key_id,
            encrypted_value=encrypted_secret
        )

        parsed_secret = github_secret.json()

        response = await self.client.put(
            url,
            headers=headers,
            data=parsed_secret
        )

        return self.check_response(response)
    
    async def delete_repository_secret(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        secret_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/secrets/{secret_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.delete(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def get_repository_variable(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        variable_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/variables/{variable_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def list_repository_variables(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/variables'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)

    async def add_repository_variable(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        variable_name: str,
        variable_value: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/variables'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        github_variable = GithubVariable(
            name=variable_name,
            value=variable_value
        )

        parsed_variable = github_variable.json()

        response = await self.client.post(
            url,
            headers=headers,
            data=parsed_variable
        )

        return self.check_response(response)
    
    async def update_repository_variable(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        variable_name: str,
        variable_value: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/variables/{variable_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        github_variable = GithubVariable(
            name=variable_name,
            value=variable_value
        )

        parsed_variable = github_variable.json()

        response = await self.client.patch(
            url,
            headers=headers,
            data=parsed_variable
        )

        return self.check_response(response)
    
    async def delete_repository_variable(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        variable_name: str,
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
    
        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/variables/{variable_name}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.delete(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def create_pull_request( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        title: str,
        description: str,
        from_branch: str,
        to_branch: str='main',
        api_version: str='2022-11-28'
    ) -> HTTPResponse:
        project_slug = await self.slugify(project_name)
        
        url = f'https://api.github.com/repos/{organization}/{project_slug}/pulls'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        pull_request = GithubPullRequest(
            title=title,
            body=description,
            head=from_branch,
            base=to_branch
        )

        pull_request_data = pull_request.json()

        response = await self.client.post(
            url,
            headers=headers,
            data=pull_request_data
        )

        return self.check_response(response)

    async def list_workflow_runs( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/runs'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.post(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def list_pull_requests( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/pulls'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def get_pull_request( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        pull_number: int,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/pulls/{pull_number}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)

    async def list_pull_request_commits( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        pull_number: int,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/pulls/{pull_number}/commits'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def get_workflow_run( 
        self,
        organization: str,
        access_token: str,
        project_name: str,
        run_id: str,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/runs/{run_id}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)

    async def get_workflow_run_jobs(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        run_id: str,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/runs/{run_id}/jobs'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)
    
    async def get_workflow(
        self,
        organization: str,
        access_token: str,
        project_name: str,
        workflow_id: str,
        api_version: str='2022-11-28'
    ):
        project_slug = await self.slugify(project_name)

        url = f'https://api.github.com/repos/{organization}/{project_slug}/actions/workflows/{workflow_id}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': f'{api_version}',
            'Accept': 'application/vnd.github+json'
        }

        response = await self.client.get(
            url,
            headers=headers
        )

        return self.check_response(response)

    async def close(self):
        self._executor.shutdown()
        await self.client.close()

    def abort(self):
        self._executor.shutdown()
        self.client.abort()
       