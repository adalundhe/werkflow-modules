import os
import pathlib
from urllib.parse import quote

from werkflow_http import HTTP
from werkflow_http.request import File
from werkflow_shell import Shell

from .models import (
    AppitoCredentials,
    AppitoGetEnviornmentRequest,
    AppitoGetEnvironmentResponse,
    AppitoUploadTableRequest,
    AppitoRegionUrlMap,
    AppitoRegionName,
)


class Appito:

    """Handles file uploads to Apptio API using API key authentication"""
    
    def __init__(
        self, 
        region: AppitoRegionName = "US",
    ):

        self._region_url_map = AppitoRegionUrlMap()

        self._base_url = self._region_url_map.get(region)
        self._client = HTTP()
        self._shell = Shell()
        
    async def upload_file(
        self,
        request: AppitoUploadTableRequest,
    ):

        if request.appito_credentials is None:
            appito_access_key = await self._shell.get_envar(
                "APPITO_ACCESS_KEY",
            )

            appito_secret_key = await self._shell.get_envar(
                "APPITO_SECRET_KEY",
            )

            request = request.model_copy(
                update={
                    'appito_credentials': AppitoCredentials(
                        appito_access_key=appito_access_key,
                        appito_secret_key=appito_secret_key,
                    )
                },
            )

        data = {}
        if request.appito_action and request.appito_force is not None:
            data['action'] = request.appito_action
            data['force'] = str(request.appito_force).lower()
        
        # Get authentication token
        auth_token = await self._authenticate(request.appito_credentials)
        if isinstance(auth_token, Exception):
            return auth_token
        
        request = await self._update_request_with_environment(
            AppitoGetEnviornmentRequest(
                auth_token=auth_token,
                domain=request.appito_domain,
                environment_id=request.appito_environment_id,
            ),
        )

        if isinstance(request, Exception):
            return request
        
        url_path = self._encode_to_url_path(request)

        err: Exception | None = None
        if isinstance(request.appito_csv_file, str):
            upload_file = File(
                name=pathlib.Path(request.appito_csv_file).stem,
                path=request.appito_csv_file,
                content_type="text/csv",
            )

            err = await self._check_filepath(upload_file.path)

        else:
            upload_file = request.appito_csv_file

        if err:
            return err

        response = await self._client.post(
            f'{self._base_url}/{url_path}', 
            data=data,
            files=[upload_file],
            headers={
                'apptio-opentoken': auth_token,
                'apptio-current-environment': request.appito_environment_id,
                'app-type': 'Flagship',
                'app-version': 'NA'
            },
        )
        
        if not response.check_success():
            return Exception(
                f'Err. - CSV upload failed - {response.status}: {response.status_message}',
            )
        
        # Parse JSON response
        result = response.json()
        if isinstance(result, Exception):
            return result
        
        # Validate response structure
        if 'message' in result:
            # This is an error response
            raise Exception(f"Apptio API Error: {result['message']}")
        
        return result

    async def _authenticate(
        self,
        credentials: AppitoCredentials,
    ):
        """
        Authenticate using API keys and get apptio-opentoken
        
        Returns:
            Authentication token for use in subsequent requests
        """
        
        response = await self._client.post(
            f"{self._base_url}/service/apikeylogin",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "apptio-current-environment": "delta"
            },
            data={
                "keyAccess": credentials.appito_access_key,
                "keySecret": credentials.appito_secret_key,
            },
        )
        
        if not response.check_success():
            return Exception(
                f'Err. - could not authenticate - {response.status}: {response.text()}',
            )
        
        # Extract the apptio-opentoken from response headers
        token: bytes | None = response.headers.get(b'apptio-opentoken')
        if token is None:
            return Exception("No apptio-opentoken found in response headers")
        
        return token.decode()
    
    async def _get_matching_environment(
        self,
        request: AppitoGetEnviornmentRequest
    ):
        
        response = await self._client.get(
            f"{self._base_url}/api/environments/{request.domain}",
            headers={
                "apptio-opentoken": request.auth_token,
                "Accept": "application/json"
            },
        )
        
        if not response.check_success():
            return Exception(
                f'Err. - environment ID fetch failed - {response.status}: {response.text()}',
            )
        
        data = response.json()
        if isinstance(data, Exception):
            return data
        
        environment_response = AppitoGetEnvironmentResponse(environments=data)

        if request.environment_id:
            for env in environment_response.environments:
                if env.id == request.environment_id:
                    return env
                
            return Exception('No matching id found.')
        
        for env in environment_response.environments:
            if env.id is not None:
                return env
            
        return Exception('No matching id found')
    
    async def _update_request_with_environment(
        self,
        environment_request: AppitoGetEnviornmentRequest,
        table_request: AppitoUploadTableRequest
    ) -> AppitoUploadTableRequest:
        environment = await self._get_matching_environment(environment_request)
        if isinstance(environment, Exception):
            return environment

        return table_request.model_copy(
            update={
                "appito_environment_id": environment.id,
            },
        )
    
    def _encode_to_url_path(
        self,
        request: AppitoUploadTableRequest,
    ) -> str:
        url_parts = [
            "domains",
            request.appito_domain,
            "projects",
            request.appito_project,
            "tables",
            request.appito_table_name,
            "dates",
            request.appito_time_period,
        ]
        
        if request.appito_action and request.appito_environment_id is not None:
            pass
        elif request.appito_action:
            url_parts.append(request.appito_action)
        elif request.appito_force is not None:
            url_parts.append("force")
        else:
            url_parts.append("overwrite")

        return '/'.join([
            quote(part, safe='') for part in url_parts
        ])
    
    async def _check_filepath(self, csv_filepath: str):
        if not await self._shell.path_is_file(csv_filepath):
            return FileNotFoundError(f"CSV file not found: {csv_filepath}")
        
        if not await self._shell.check_file_access(
            csv_filepath,
            os.R_OK,
        ):
            return PermissionError(f"Cannot read CSV file: {csv_filepath}")
        
        # Validate file extension
        file_ext = pathlib.Path(csv_filepath).suffix.lower()
        supported_formats = ['.csv', '.tsv', '.csv.gz', '.tsv.gz']
        if file_ext not in supported_formats:
            return ValueError(f"Unsupported file format: {file_ext}. Supported formats: {', '.join(supported_formats)}")
        
