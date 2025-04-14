import asyncio
import boto3
import functools
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegion,
)
from werkflow_aws.models.cost_explorer import CostExplorerQuery, CostExplorerResponse
from werkflow_aws.types import CostExplorerClient
from werkflow.modules.system import System
from typing import Union


class AWSCostExplorer:
    
    def __init__(self) -> None:
        
        self._system = System()

        self._loop: Union[asyncio.AbstractEventLoop, None] = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'CostExplorer'

    async def connect(
        self,
        credentials: AWSCredentialsSet,
        region: AWSRegion
    ):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._client: CostExplorerClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'codeartifact',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region=region.value
                )
            )
        )

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

    async def get_cost_and_usage(
        self,
        query: CostExplorerQuery
    ) -> CostExplorerResponse:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name,
            )
        
        dumped = query.model_dump(exclude_none=True)
        
        result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_cost_and_usage,
                TimePeriod=dumped.get('TimePeriod'),
                Granularity=dumped.get('Granularity'),
                Metrics=dumped.get('Metrics'),
                Filter=dumped.get('Filter'),
                GroupBy=dumped.get('GroupBy'),
                BillingViewArn=dumped.get('BillingViewArn'),
                NextPageToken=dumped.get('NextPageToken')
            )
        )

        return CostExplorerResponse(**result)
    
    async def close(self):

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