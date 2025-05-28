import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor

import boto3
from botocore.config import Config
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_aws.models.sts import (
    AssumeRoleRequest,
    AssumedRoleResponse,
)
from werkflow_system import System
from werkflow_aws.types import STSClient


class AWSSTS:

    def __init__(self):
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'STS'

        self._regions = AWSRegionMap()

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()       

        self._client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def connect_unauthorized(
        self,
        region: RegionName,
    ):
        
        aws_region = self._regions.get(region)

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: STSClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'sts',
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    async def assume_role(
        self,
        assume_role_request: AssumeRoleRequest
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name
            )

        response = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.assume_role,
                **assume_role_request.model_dump(exclude_none=True)
            )
        )

        return AssumedRoleResponse(**response)
    
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