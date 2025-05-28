import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.exceptions import (
    EmptyResponseException,
    UnsetAWSConnectionException
)
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_aws.types import (
    CodeArtifactClient,
    CodeArtifactFormat
)
from werkflow_system import System
from typing import Union


class AWSCodeArtifact:
    
    def __init__(self) -> None:
        
        self._system = System()

        self._loop: Union[asyncio.AbstractEventLoop, None] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'CodeArtifact'
        self._regions = AWSRegionMap()

    async def sso(
        self,
        profile_name: str,
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name
            )
        )

        self._client: CodeArtifactClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'codeartifact',
            )
        )


    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: CodeArtifactClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'codeartifact',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def get_authorization_token(
        self,
        domain: str,
        domain_owner: str,
        duration_seconds: int=1000
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )

        result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_authorization_token,
                domain=domain,
                domainOwner=domain_owner,
                durationSeconds=duration_seconds
            )
        )

        authorization_token = result.get('authorizationToken')

        if authorization_token is None:
            raise EmptyResponseException(
                self.service_name,
                'get_authorization_token',
                'authorizationToken'
            )
        
        return authorization_token
    
    async def get_repository_endpoint(
        self,
        domain: str,
        domain_owner: str,
        repository: str,
        repository_format: CodeArtifactFormat
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            ) 
        
        result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_repository_endpoint,
                domain=domain,
                domainOwner=domain_owner,
                repository=repository,
                format=repository_format
            )
        )

        endpoint = result.get('repositoryEndpoint')

        if endpoint is None:
            raise EmptyResponseException(
                self.service_name,
                'get_repository_endpoint',
                'repositoryEndpoint'
            )

        return endpoint

    async def close(self):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client:
            await self._loop.run_in_executor(
                None,
                self._client.close
            )

        await self._system.close()
        self._executor.shutdown()

    def abort(self):
        self._client.close()
        self._system.abort()
        self._executor.shutdown()