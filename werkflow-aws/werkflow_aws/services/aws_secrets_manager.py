import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)

from werkflow_aws.models.secrets_manager import (
    AWSSecretManagerGetSecretValueResponse,
    AWSSecretsManagerGetSecretValueRequest,
)


from werkflow_aws.types import SecretsManagerClient


from werkflow_system import System


class AWSSecretsManager:
    
    def __init__(self) -> None:
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client: SecretsManagerClient | None = None

        self.service_name = 'SecretsManager'
        self._regions = AWSRegionMap()
    
    async def sso(
        self,
        profile_name: str,
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        await self._loop.run_in_executor(
            None,
            functools.partial(
                boto3.setup_default_session,
                profile_name=profile_name
            )
        )

        self._client: SecretsManagerClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'secretsmanager',
            )
        )

    async def connect(
        self,
        region: RegionName,
        credentials: AWSCredentialsSet | None = None,
    ):
        
        aws_region = self._regions.get(region)

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        credentials_data: dict[str, str] = {}
        if credentials:
            credentials_data = credentials.model_dump(
                exclude='aws_profile'
            )

        self._client: SecretsManagerClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'secretsmanager',
                config=Config(
                    region_name=aws_region.value
                )
                **credentials_data,
            )
        )

    async def get_secret_value(
        self,
        request: AWSSecretsManagerGetSecretValueRequest,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )
        
        dumped = request.model_dump(exclude_none=True)

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_secret_value,
                **dumped
            )
        )

        return AWSSecretManagerGetSecretValueResponse(**response)

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