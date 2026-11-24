from werkflow_aws.models.codecatalyst import (
    CodeCatalystCreateAccessTokenRequest,
    CodeCatalystCreateAccessTokenResponse,
    CodeCatalystCreateDevEnvironmentRequest,
    CodeCatalystCreateDevEnvironmentResponse,
    CodeCatalystCreateProjectRequest,
    CodeCatalystCreateProjectResponse,
    CodeCatalystCreateSourceRepositoryBranchRequest,
    CodeCatalystCreateSourceRepositoryBranchResponse,
    CodeCatalystCreateSourceRepositoryRequest,
    CodeCatalystCreateSourceRepositoryResponse,
    CodeCatalystDeleteAccessTokenRequest,
    CodeCatalystDeleteAccessTokenResponse,
    CodeCatalystDeleteDevEnvironmentRequest,
    CodeCatalystDeleteDevEnvironmentResponse,
    CodeCatalystDeleteProjectRequest,
    CodeCatalystDeleteProjectResponse,
    CodeCatalystDeleteSourceRepositoryRequest,
    CodeCatalystDeleteSourceRepositoryResponse,
    CodeCatalystDeleteSpaceRequest,
    CodeCatalystDeleteSpaceResponse,
    CodeCatalystGetDevEnvironmentRequest,
    CodeCatalystGetDevEnvironmentResponse,
    CodeCatalystGetProjectRequest,
    CodeCatalystGetProjectResponse,
    CodeCatalystGetSourceRepositoryCloneUrlsRequest,
    CodeCatalystGetSourceRepositoryCloneUrlsResponse,
    CodeCatalystGetSourceRepositoryRequest,
    CodeCatalystGetSourceRepositoryResponse,
    CodeCatalystGetSpaceRequest,
    CodeCatalystGetSpaceResponse,
    CodeCatalystGetSubscriptionRequest,
    CodeCatalystGetSubscriptionResponse,
    CodeCatalystGetUserDetailsRequest,
    CodeCatalystGetUserDetailsResponse,
    CodeCatalystGetWorkflowRequest,
    CodeCatalystGetWorkflowResponse,
    CodeCatalystGetWorkflowRunRequest,
    CodeCatalystGetWorkflowRunResponse,
    CodeCatalystListAccessTokensRequest,
    CodeCatalystListAccessTokensResponse,
    CodeCatalystListDevEnvironmentSessionsRequest,
    CodeCatalystListDevEnvironmentSessionsResponse,
    CodeCatalystListDevEnvironmentsRequest,
    CodeCatalystListDevEnvironmentsResponse,
    CodeCatalystListEventLogsRequest,
    CodeCatalystListEventLogsResponse,
    CodeCatalystListProjectsRequest,
    CodeCatalystListProjectsResponse,
    CodeCatalystListSourceRepositoriesRequest,
    CodeCatalystListSourceRepositoriesResponse,
    CodeCatalystListSourceRepositoryBranchesRequest,
    CodeCatalystListSourceRepositoryBranchesResponse,
    CodeCatalystListSpacesRequest,
    CodeCatalystListSpacesResponse,
    CodeCatalystListWorkflowRunsRequest,
    CodeCatalystListWorkflowRunsResponse,
    CodeCatalystListWorkflowsRequest,
    CodeCatalystListWorkflowsResponse,
    CodeCatalystStartDevEnvironmentRequest,
    CodeCatalystStartDevEnvironmentResponse,
    CodeCatalystStartDevEnvironmentSessionRequest,
    CodeCatalystStartDevEnvironmentSessionResponse,
    CodeCatalystStartWorkflowRunRequest,
    CodeCatalystStartWorkflowRunResponse,
    CodeCatalystStopDevEnvironmentRequest,
    CodeCatalystStopDevEnvironmentResponse,
    CodeCatalystStopDevEnvironmentSessionRequest,
    CodeCatalystStopDevEnvironmentSessionResponse,
    CodeCatalystUpdateDevEnvironmentRequest,
    CodeCatalystUpdateDevEnvironmentResponse,
    CodeCatalystUpdateProjectRequest,
    CodeCatalystUpdateProjectResponse,
    CodeCatalystUpdateSpaceRequest,
    CodeCatalystUpdateSpaceResponse,
    CodeCatalystVerifySessionRequest,
    CodeCatalystVerifySessionResponse,
)
from werkflow_aws.types.codecatalyst_client import CodeCatalystClient
from .base import AWSBaseService


class AWSCodeCatalyst(AWSBaseService[CodeCatalystClient]):
    service_name = 'codecatalyst'
    boto3_service_name = 'codecatalyst'

    def __init__(self) -> None:
        super().__init__(service_name='codecatalyst', boto3_service_name='codecatalyst')

    async def create_access_token(
        self,
        request: CodeCatalystCreateAccessTokenRequest,
    ) -> CodeCatalystCreateAccessTokenResponse:
        client = self._require_client()
        return await self._execute(client.create_access_token, request, CodeCatalystCreateAccessTokenResponse)

    async def create_dev_environment(
        self,
        request: CodeCatalystCreateDevEnvironmentRequest,
    ) -> CodeCatalystCreateDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.create_dev_environment, request, CodeCatalystCreateDevEnvironmentResponse)

    async def create_project(
        self,
        request: CodeCatalystCreateProjectRequest,
    ) -> CodeCatalystCreateProjectResponse:
        client = self._require_client()
        return await self._execute(client.create_project, request, CodeCatalystCreateProjectResponse)

    async def create_source_repository(
        self,
        request: CodeCatalystCreateSourceRepositoryRequest,
    ) -> CodeCatalystCreateSourceRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.create_source_repository, request, CodeCatalystCreateSourceRepositoryResponse)

    async def create_source_repository_branch(
        self,
        request: CodeCatalystCreateSourceRepositoryBranchRequest,
    ) -> CodeCatalystCreateSourceRepositoryBranchResponse:
        client = self._require_client()
        return await self._execute(client.create_source_repository_branch, request, CodeCatalystCreateSourceRepositoryBranchResponse)

    async def delete_access_token(
        self,
        request: CodeCatalystDeleteAccessTokenRequest,
    ) -> CodeCatalystDeleteAccessTokenResponse:
        client = self._require_client()
        return await self._execute(client.delete_access_token, request, CodeCatalystDeleteAccessTokenResponse)

    async def delete_dev_environment(
        self,
        request: CodeCatalystDeleteDevEnvironmentRequest,
    ) -> CodeCatalystDeleteDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_dev_environment, request, CodeCatalystDeleteDevEnvironmentResponse)

    async def delete_project(
        self,
        request: CodeCatalystDeleteProjectRequest,
    ) -> CodeCatalystDeleteProjectResponse:
        client = self._require_client()
        return await self._execute(client.delete_project, request, CodeCatalystDeleteProjectResponse)

    async def delete_source_repository(
        self,
        request: CodeCatalystDeleteSourceRepositoryRequest,
    ) -> CodeCatalystDeleteSourceRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.delete_source_repository, request, CodeCatalystDeleteSourceRepositoryResponse)

    async def delete_space(
        self,
        request: CodeCatalystDeleteSpaceRequest,
    ) -> CodeCatalystDeleteSpaceResponse:
        client = self._require_client()
        return await self._execute(client.delete_space, request, CodeCatalystDeleteSpaceResponse)

    async def get_dev_environment(
        self,
        request: CodeCatalystGetDevEnvironmentRequest,
    ) -> CodeCatalystGetDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.get_dev_environment, request, CodeCatalystGetDevEnvironmentResponse)

    async def get_project(
        self,
        request: CodeCatalystGetProjectRequest,
    ) -> CodeCatalystGetProjectResponse:
        client = self._require_client()
        return await self._execute(client.get_project, request, CodeCatalystGetProjectResponse)

    async def get_source_repository(
        self,
        request: CodeCatalystGetSourceRepositoryRequest,
    ) -> CodeCatalystGetSourceRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.get_source_repository, request, CodeCatalystGetSourceRepositoryResponse)

    async def get_source_repository_clone_urls(
        self,
        request: CodeCatalystGetSourceRepositoryCloneUrlsRequest,
    ) -> CodeCatalystGetSourceRepositoryCloneUrlsResponse:
        client = self._require_client()
        return await self._execute(client.get_source_repository_clone_urls, request, CodeCatalystGetSourceRepositoryCloneUrlsResponse)

    async def get_space(
        self,
        request: CodeCatalystGetSpaceRequest,
    ) -> CodeCatalystGetSpaceResponse:
        client = self._require_client()
        return await self._execute(client.get_space, request, CodeCatalystGetSpaceResponse)

    async def get_subscription(
        self,
        request: CodeCatalystGetSubscriptionRequest,
    ) -> CodeCatalystGetSubscriptionResponse:
        client = self._require_client()
        return await self._execute(client.get_subscription, request, CodeCatalystGetSubscriptionResponse)

    async def get_user_details(
        self,
        request: CodeCatalystGetUserDetailsRequest | None = None,
    ) -> CodeCatalystGetUserDetailsResponse:
        client = self._require_client()
        return await self._execute(client.get_user_details, request, CodeCatalystGetUserDetailsResponse)

    async def get_workflow(
        self,
        request: CodeCatalystGetWorkflowRequest,
    ) -> CodeCatalystGetWorkflowResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow, request, CodeCatalystGetWorkflowResponse)

    async def get_workflow_run(
        self,
        request: CodeCatalystGetWorkflowRunRequest,
    ) -> CodeCatalystGetWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.get_workflow_run, request, CodeCatalystGetWorkflowRunResponse)

    async def list_access_tokens(
        self,
        request: CodeCatalystListAccessTokensRequest | None = None,
    ) -> CodeCatalystListAccessTokensResponse:
        client = self._require_client()
        return await self._execute(client.list_access_tokens, request, CodeCatalystListAccessTokensResponse)

    async def list_access_tokens_paginated(
        self,
        request: CodeCatalystListAccessTokensRequest | None = None,
    ) -> list[CodeCatalystListAccessTokensResponse]:
        return await self._paginate('list_access_tokens', request, CodeCatalystListAccessTokensResponse)

    async def list_dev_environment_sessions(
        self,
        request: CodeCatalystListDevEnvironmentSessionsRequest,
    ) -> CodeCatalystListDevEnvironmentSessionsResponse:
        client = self._require_client()
        return await self._execute(client.list_dev_environment_sessions, request, CodeCatalystListDevEnvironmentSessionsResponse)

    async def list_dev_environment_sessions_paginated(
        self,
        request: CodeCatalystListDevEnvironmentSessionsRequest,
    ) -> list[CodeCatalystListDevEnvironmentSessionsResponse]:
        return await self._paginate('list_dev_environment_sessions', request, CodeCatalystListDevEnvironmentSessionsResponse)

    async def list_dev_environments(
        self,
        request: CodeCatalystListDevEnvironmentsRequest,
    ) -> CodeCatalystListDevEnvironmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_dev_environments, request, CodeCatalystListDevEnvironmentsResponse)

    async def list_dev_environments_paginated(
        self,
        request: CodeCatalystListDevEnvironmentsRequest,
    ) -> list[CodeCatalystListDevEnvironmentsResponse]:
        return await self._paginate('list_dev_environments', request, CodeCatalystListDevEnvironmentsResponse)

    async def list_event_logs(
        self,
        request: CodeCatalystListEventLogsRequest,
    ) -> CodeCatalystListEventLogsResponse:
        client = self._require_client()
        return await self._execute(client.list_event_logs, request, CodeCatalystListEventLogsResponse)

    async def list_event_logs_paginated(
        self,
        request: CodeCatalystListEventLogsRequest,
    ) -> list[CodeCatalystListEventLogsResponse]:
        return await self._paginate('list_event_logs', request, CodeCatalystListEventLogsResponse)

    async def list_projects(
        self,
        request: CodeCatalystListProjectsRequest,
    ) -> CodeCatalystListProjectsResponse:
        client = self._require_client()
        return await self._execute(client.list_projects, request, CodeCatalystListProjectsResponse)

    async def list_projects_paginated(
        self,
        request: CodeCatalystListProjectsRequest,
    ) -> list[CodeCatalystListProjectsResponse]:
        return await self._paginate('list_projects', request, CodeCatalystListProjectsResponse)

    async def list_source_repositories(
        self,
        request: CodeCatalystListSourceRepositoriesRequest,
    ) -> CodeCatalystListSourceRepositoriesResponse:
        client = self._require_client()
        return await self._execute(client.list_source_repositories, request, CodeCatalystListSourceRepositoriesResponse)

    async def list_source_repositories_paginated(
        self,
        request: CodeCatalystListSourceRepositoriesRequest,
    ) -> list[CodeCatalystListSourceRepositoriesResponse]:
        return await self._paginate('list_source_repositories', request, CodeCatalystListSourceRepositoriesResponse)

    async def list_source_repository_branches(
        self,
        request: CodeCatalystListSourceRepositoryBranchesRequest,
    ) -> CodeCatalystListSourceRepositoryBranchesResponse:
        client = self._require_client()
        return await self._execute(client.list_source_repository_branches, request, CodeCatalystListSourceRepositoryBranchesResponse)

    async def list_source_repository_branches_paginated(
        self,
        request: CodeCatalystListSourceRepositoryBranchesRequest,
    ) -> list[CodeCatalystListSourceRepositoryBranchesResponse]:
        return await self._paginate('list_source_repository_branches', request, CodeCatalystListSourceRepositoryBranchesResponse)

    async def list_spaces(
        self,
        request: CodeCatalystListSpacesRequest | None = None,
    ) -> CodeCatalystListSpacesResponse:
        client = self._require_client()
        return await self._execute(client.list_spaces, request, CodeCatalystListSpacesResponse)

    async def list_spaces_paginated(
        self,
        request: CodeCatalystListSpacesRequest | None = None,
    ) -> list[CodeCatalystListSpacesResponse]:
        return await self._paginate('list_spaces', request, CodeCatalystListSpacesResponse)

    async def list_workflow_runs(
        self,
        request: CodeCatalystListWorkflowRunsRequest,
    ) -> CodeCatalystListWorkflowRunsResponse:
        client = self._require_client()
        return await self._execute(client.list_workflow_runs, request, CodeCatalystListWorkflowRunsResponse)

    async def list_workflow_runs_paginated(
        self,
        request: CodeCatalystListWorkflowRunsRequest,
    ) -> list[CodeCatalystListWorkflowRunsResponse]:
        return await self._paginate('list_workflow_runs', request, CodeCatalystListWorkflowRunsResponse)

    async def list_workflows(
        self,
        request: CodeCatalystListWorkflowsRequest,
    ) -> CodeCatalystListWorkflowsResponse:
        client = self._require_client()
        return await self._execute(client.list_workflows, request, CodeCatalystListWorkflowsResponse)

    async def list_workflows_paginated(
        self,
        request: CodeCatalystListWorkflowsRequest,
    ) -> list[CodeCatalystListWorkflowsResponse]:
        return await self._paginate('list_workflows', request, CodeCatalystListWorkflowsResponse)

    async def start_dev_environment(
        self,
        request: CodeCatalystStartDevEnvironmentRequest,
    ) -> CodeCatalystStartDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.start_dev_environment, request, CodeCatalystStartDevEnvironmentResponse)

    async def start_dev_environment_session(
        self,
        request: CodeCatalystStartDevEnvironmentSessionRequest,
    ) -> CodeCatalystStartDevEnvironmentSessionResponse:
        client = self._require_client()
        return await self._execute(client.start_dev_environment_session, request, CodeCatalystStartDevEnvironmentSessionResponse)

    async def start_workflow_run(
        self,
        request: CodeCatalystStartWorkflowRunRequest,
    ) -> CodeCatalystStartWorkflowRunResponse:
        client = self._require_client()
        return await self._execute(client.start_workflow_run, request, CodeCatalystStartWorkflowRunResponse)

    async def stop_dev_environment(
        self,
        request: CodeCatalystStopDevEnvironmentRequest,
    ) -> CodeCatalystStopDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.stop_dev_environment, request, CodeCatalystStopDevEnvironmentResponse)

    async def stop_dev_environment_session(
        self,
        request: CodeCatalystStopDevEnvironmentSessionRequest,
    ) -> CodeCatalystStopDevEnvironmentSessionResponse:
        client = self._require_client()
        return await self._execute(client.stop_dev_environment_session, request, CodeCatalystStopDevEnvironmentSessionResponse)

    async def update_dev_environment(
        self,
        request: CodeCatalystUpdateDevEnvironmentRequest,
    ) -> CodeCatalystUpdateDevEnvironmentResponse:
        client = self._require_client()
        return await self._execute(client.update_dev_environment, request, CodeCatalystUpdateDevEnvironmentResponse)

    async def update_project(
        self,
        request: CodeCatalystUpdateProjectRequest,
    ) -> CodeCatalystUpdateProjectResponse:
        client = self._require_client()
        return await self._execute(client.update_project, request, CodeCatalystUpdateProjectResponse)

    async def update_space(
        self,
        request: CodeCatalystUpdateSpaceRequest,
    ) -> CodeCatalystUpdateSpaceResponse:
        client = self._require_client()
        return await self._execute(client.update_space, request, CodeCatalystUpdateSpaceResponse)

    async def verify_session(
        self,
        request: CodeCatalystVerifySessionRequest | None = None,
    ) -> CodeCatalystVerifySessionResponse:
        client = self._require_client()
        return await self._execute(client.verify_session, request, CodeCatalystVerifySessionResponse)
