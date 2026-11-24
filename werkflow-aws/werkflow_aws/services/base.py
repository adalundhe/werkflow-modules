from __future__ import annotations

import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Generic, TypeVar

import boto3
from botocore.config import Config
from pydantic import BaseModel

from werkflow_aws.exceptions import UnsetAWSConnectionException
from werkflow_aws.helpers import collect_paginator
from werkflow_aws.models import (
    AWSCredentialsSet,
    AWSRegionMap,
    RegionName,
)
from werkflow_system import System


ClientT = TypeVar('ClientT')
ResponseT = TypeVar('ResponseT', bound=BaseModel)


class AWSBaseService(Generic[ClientT]):
    service_name: str = ''
    boto3_service_name: str = ''

    def __init__(
        self,
        service_name: str | None = None,
        boto3_service_name: str | None = None,
    ) -> None:
        self._system = System()
        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )
        self._client: ClientT | None = None
        if service_name is not None:
            self.service_name = service_name
        if boto3_service_name is not None:
            self.boto3_service_name = boto3_service_name
        self._regions = AWSRegionMap()

    def _get_loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None or self._loop.is_closed():
            self._loop = asyncio.get_running_loop()
        return self._loop

    def _require_client(self) -> ClientT:
        if self._client is None:
            raise UnsetAWSConnectionException(self.service_name)
        return self._client

    async def sso(
        self,
        profile_name: str,
        region: RegionName | None = None,
    ) -> None:
        loop = self._get_loop()
        region_name = self._regions.get(region).value if region is not None else None

        def _create_sso_client() -> Any:
            session = boto3.Session(
                profile_name=profile_name,
                region_name=region_name,
            )
            config = Config(region_name=region_name) if region_name is not None else None
            return session.client(self.boto3_service_name, config=config)

        self._client = await loop.run_in_executor(self._executor, _create_sso_client)

    async def connect(
        self,
        region: RegionName,
        credentials: AWSCredentialsSet | None = None,
    ) -> None:
        aws_region = self._regions.get(region)
        loop = self._get_loop()

        credentials_data: dict[str, Any] = {}
        if credentials is not None:
            credentials_data = credentials.model_dump(
                exclude={'aws_profile'},
                exclude_none=True,
            )

        self._client = await loop.run_in_executor(
            self._executor,
            functools.partial(
                boto3.client,
                self.boto3_service_name,
                config=Config(region_name=aws_region.value),
                **credentials_data,
            ),
        )

    async def _execute(
        self,
        method: Callable[..., dict[str, Any]],
        request: BaseModel | None,
        response_model: type[ResponseT],
    ) -> ResponseT:
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True) if request is not None else {}
        response = await loop.run_in_executor(
            self._executor,
            functools.partial(method, **dumped),
        )
        return response_model(**response)

    async def _execute_raw(
        self,
        method: Callable[..., Any],
        request: BaseModel | None = None,
    ) -> Any:
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True) if request is not None else {}
        return await loop.run_in_executor(
            self._executor,
            functools.partial(method, **dumped),
        )

    async def _paginate(
        self,
        operation: str,
        request: BaseModel | None,
        response_model: type[ResponseT],
    ) -> list[ResponseT]:
        client: Any = self._require_client()
        loop = self._get_loop()
        dumped = request.model_dump(exclude_none=True) if request is not None else {}

        paginator = await loop.run_in_executor(
            self._executor,
            functools.partial(client.get_paginator, operation),
        )
        pagination_result = await loop.run_in_executor(
            self._executor,
            functools.partial(paginator.paginate, **dumped),
        )
        results = await loop.run_in_executor(
            self._executor,
            functools.partial(collect_paginator, pagination_result),
        )
        return [response_model(**result) for result in results]

    async def close(self) -> None:
        if self._client is not None:
            client: Any = self._client
            self._client = None
            try:
                loop = self._get_loop()
                await loop.run_in_executor(None, client.close)
            except RuntimeError:
                client.close()

        await self._system.close()
        try:
            loop = self._get_loop()
            await loop.run_in_executor(None, self._executor.shutdown, True)
        except RuntimeError:
            self._executor.shutdown(wait=True)

    def abort(self) -> None:
        if self._client is not None:
            client: Any = self._client
            self._client = None
            client.close()

        self._system.abort()
        self._executor.shutdown(wait=False, cancel_futures=True)
