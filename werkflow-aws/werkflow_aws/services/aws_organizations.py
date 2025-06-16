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
from werkflow_aws.models.organizations import (
    OrganizationsListAccountsRequest,
    OrganizationsListAccountsResponse,
)
from werkflow_aws.helpers import collect_paginator
from werkflow_aws.types import OrganizationsClient

from werkflow_system import System


class AWSOrganizations:
    
    def __init__(self) -> None:
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'Organizations'
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

        self._client: OrganizationsClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'organizations',
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

        self._client: OrganizationsClient = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                'organizations',
                aws_access_key_id=credentials.aws_access_key_id,
                aws_secret_access_key=credentials.aws_secret_access_key,
                aws_session_token=credentials.aws_session_token,
                config=Config(
                    region_name=aws_region.value
                )
            )
        )

    
    async def list_accounts(
        self,
        request: OrganizationsListAccountsRequest
    ) -> OrganizationsListAccountsResponse:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name,
            )
        
        dumped = request.model_dump(exclude_none=True)
        
        result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.list_accounts,
                **dumped
            )
        )

        return OrganizationsListAccountsResponse(**result)

    async def list_accounts_paginated(
        self,
        request: OrganizationsListAccountsRequest
    ) -> list[OrganizationsListAccountsResponse]:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._client is None:
            raise UnsetAWSConnectionException(
                self.service_name,
            )
        
        dumped = request.model_dump(exclude_none=True)

        paginator = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._client.get_paginator,
                'list_accounts',
            )
        )

        pagination_result = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                paginator.paginate,
                **dumped
            )
        )

        results = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                collect_paginator,
                pagination_result,
            )
        )

        return [
            OrganizationsListAccountsResponse(
                Accounts=result['Accounts'],
            ) for result in results
        ]
    
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