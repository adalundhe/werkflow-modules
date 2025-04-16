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
from werkflow_aws.types import (
    CostExplorerClient,
    STSClient,
)
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
        self._session: boto3.Session | None = None

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
                'ce',
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

        self._client: CostExplorerClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'ce',
            )
        )

    async def assume_role(
        self,
        role_arn: str,
        role_session_name: str,
        role_external_id: str,
        region_name: str,
    ):
        
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self._session = boto3.Session(region_name=region_name)
        sts_client: STSClient = self._session.client('sts', region_name=region_name)
        
        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            ExternalId=role_external_id
        )
        self.current_role_details = {
            'role_arn': role_arn,
            'external_id': role_external_id,
            'source_profile': 'N/A'  # Assuming source_profile is not available here
        }

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
        
        dumped = query.dump()
        
        result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_cost_and_usage,
                **dumped
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