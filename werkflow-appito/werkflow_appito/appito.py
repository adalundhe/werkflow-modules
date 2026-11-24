import os
import pathlib
from typing import Any
from urllib.parse import quote

from pydantic import JsonValue
from werkflow_core import Module
from werkflow_http import HTTP
from werkflow_http.request import File
from werkflow_shell import Shell

from .models import (
    AppitoCredentials,
    AppitoEnvironment,
    AppitoGetEnvironmentRequest,
    AppitoGetEnvironmentResponse,
    AppitoRegionName,
    AppitoRegionUrlMap,
    AppitoUploadTableRequest,
)


class Appito(Module):
    """Handles file uploads to Apptio API using API key authentication."""

    module_enabled = True
    dependencies = [
        'werkflow-http',
        'werkflow-shell',
        'pydantic',
    ]

    def __init__(
        self,
        region: AppitoRegionName = "US",
    ) -> None:
        super().__init__()
        self._region_url_map = AppitoRegionUrlMap()
        self._base_url = self._region_url_map.get(region)
        self._client = HTTP()
        self._shell = Shell()

    async def upload_file(
        self,
        request: AppitoUploadTableRequest,
    ) -> JsonValue | Exception:
        if request.appito_credentials is None:
            appito_access_key = (
                await self._shell.get_envar("APPITO_ACCESS_KEY")
                or await self._shell.get_envar("APPTIO_ACCESS_KEY")
            )
            appito_secret_key = (
                await self._shell.get_envar("APPITO_SECRET_KEY")
                or await self._shell.get_envar("APPTIO_SECRET_KEY")
            )
            appito_current_environment = (
                await self._shell.get_envar("APPITO_CURRENT_ENVIRONMENT")
                or await self._shell.get_envar("APPTIO_CURRENT_ENVIRONMENT")
            )

            request = request.model_copy(
                update={
                    'appito_credentials': AppitoCredentials(
                        appito_access_key=appito_access_key,
                        appito_secret_key=appito_secret_key,
                        appito_current_environment=appito_current_environment,
                    )
                },
            )

        assert request.appito_credentials is not None

        data: dict[str, Any] = {}
        if request.appito_action and request.appito_force is not None:
            data['action'] = request.appito_action
            data['force'] = str(request.appito_force).lower()

        # Get authentication token
        auth_token = await self._authenticate(request.appito_credentials)
        if isinstance(auth_token, Exception):
            return auth_token

        updated_request = await self._update_request_with_environment(
            AppitoGetEnvironmentRequest(
                auth_token=auth_token,
                domain=request.appito_domain,
                environment_id=request.appito_environment_id,
            ),
            request,
        )

        if isinstance(updated_request, Exception):
            return updated_request

        request = updated_request
        url_path = self._encode_to_url_path(request)

        err: Exception | None = None
        if isinstance(request.appito_csv_file, str):
            err = await self._check_filepath(request.appito_csv_file)
            if err is not None:
                return err

            is_gzip = request.appito_csv_file.lower().endswith('.gz')
            upload_file = File(
                name=pathlib.Path(request.appito_csv_file).stem,
                path=request.appito_csv_file,
                content_type="application/gzip" if is_gzip else "text/csv",
                mode='rb' if is_gzip else 'r',
            )
        else:
            upload_file = request.appito_csv_file
            if upload_file.data is None and upload_file.path is not None:
                err = await self._check_filepath(upload_file.path)
                if err is not None:
                    return err

        upload_headers: dict[str, str | bytes | int | float | None] = {
            'apptio-opentoken': auth_token,
            'app-type': 'Flagship',
            'app-version': 'NA',
        }
        if request.appito_environment_id is not None:
            upload_headers['apptio-current-environment'] = request.appito_environment_id

        response = await self._client.post(
            f'{self._base_url}/{url_path}',
            data=data if data else None,
            files=[upload_file],
            headers=upload_headers,
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
        if isinstance(result, dict) and 'message' in result:
            raise Exception(f"Apptio API Error: {result['message']}")

        return result

    async def _authenticate(
        self,
        credentials: AppitoCredentials,
    ) -> str | Exception:
        """Authenticate using API keys and get apptio-opentoken."""
        headers: dict[str, str | bytes | int | float | None] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if credentials.appito_current_environment is not None:
            headers["apptio-current-environment"] = credentials.appito_current_environment

        response = await self._client.post(
            f"{self._base_url}/service/apikeylogin",
            headers=headers,
            data={
                "keyAccess": credentials.appito_access_key,
                "keySecret": credentials.appito_secret_key,
            },
        )

        if not response.check_success():
            return Exception(
                f'Err. - could not authenticate - {response.status}: {response.text()}',
            )

        token: bytes | None = response.headers.get(b'apptio-opentoken')
        if token is None:
            return Exception("No apptio-opentoken found in response headers")

        return token.decode('utf-8')

    async def _get_matching_environment(
        self,
        request: AppitoGetEnvironmentRequest,
    ) -> AppitoEnvironment | Exception:
        response = await self._client.get(
            f"{self._base_url}/api/environments/{request.domain}",
            headers={
                "apptio-opentoken": request.auth_token,
                "Accept": "application/json",
            },
        )

        if not response.check_success():
            return Exception(
                f'Err. - environment ID fetch failed - {response.status}: {response.text()}',
            )

        data = response.json()
        if isinstance(data, Exception):
            return data

        if not isinstance(data, list):
            return Exception(
                f'Err. - unexpected environments response type: {type(data).__name__}',
            )

        environment_response = AppitoGetEnvironmentResponse(
            environments=[
                AppitoEnvironment.model_validate(item)
                for item in data
            ]
        )

        if request.environment_id:
            for env in environment_response.environments:
                if env.id == request.environment_id:
                    return env

            return Exception('No matching id found.')

        for env in environment_response.environments:
            if env.id is not None:
                return env

        return Exception('No matching id found.')

    async def _update_request_with_environment(
        self,
        environment_request: AppitoGetEnvironmentRequest,
        table_request: AppitoUploadTableRequest,
    ) -> AppitoUploadTableRequest | Exception:
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

        if request.appito_action and request.appito_force is not None:
            pass
        elif request.appito_action:
            url_parts.append(request.appito_action)
        elif request.appito_force is not None:
            url_parts.append("force")
        else:
            url_parts.append("overwrite")

        return '/'.join(
            quote(part, safe='') for part in url_parts
        )

    async def _check_filepath(self, csv_filepath: str) -> Exception | None:
        if not await self._shell.check_if_is_file(csv_filepath):
            return FileNotFoundError(f"CSV file not found: {csv_filepath}")

        if not await self._shell.check_file_access(
            csv_filepath,
            os.R_OK,
        ):
            return PermissionError(f"Cannot read CSV file: {csv_filepath}")

        path_obj = pathlib.Path(csv_filepath)
        suffixes = [suffix.lower() for suffix in path_obj.suffixes]
        compound_ext = ''.join(suffixes[-2:]) if len(suffixes) >= 2 else ''
        file_ext = suffixes[-1] if suffixes else ''
        supported_formats = ('.csv', '.tsv', '.csv.gz', '.tsv.gz')
        if compound_ext not in supported_formats and file_ext not in supported_formats:
            detected = compound_ext or file_ext
            return ValueError(
                f"Unsupported file format: {detected}. Supported formats: {', '.join(supported_formats)}"
            )

        return None

    async def close(self) -> None:
        await self._client.close()
        await self._shell.close()

    def abort(self) -> None:
        self._client.abort()
        self._shell.abort()
