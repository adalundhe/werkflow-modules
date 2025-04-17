import asyncio
from typing import Dict

import orjson
from werkflow_core import Module

from .connections.http import MercurySyncHTTPConnection
from .request import (
    Data,
    Headers,
    Params,
    Request,
    RequestWithData,
)


class HTTP(Module):
    dependencies=[
        'aiodns',
        'orjson',
        'pydantic',
    ]

    def __init__(self) -> None:
        super().__init__()
        self._client: MercurySyncHTTPConnection = None

    async def get(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params
        )

        return await self._client.get(
            url,
            auth=auth,
            headers=headers,
            params=params
        )
    
    async def post(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers: Dict[str, str] | None = None
        if headers:
            lowered_headers = {
                header_key.lower(): header_value for header_key, header_value in headers.items()
            }

        if lowered_headers and lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data)

        return await self._client.post(
            url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )
    
    async def put(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers: Dict[str, str] | None = None
        if headers:
            lowered_headers = {
                header_key.lower(): header_value for header_key, header_value in headers.items()
            }

        if lowered_headers and lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data).decode()

        return await self._client.put(
            url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )
    
    async def patch(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers: Dict[str, str] | None = None
        if headers:
            lowered_headers = {
                header_key.lower(): header_value for header_key, header_value in headers.items()
            }

        if lowered_headers and lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data).decode()

        return await self._client.patch(
            url,
            auth=auth,
            headers=headers,
            params=params,
            data=data
        )
    
    async def delete(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params
        )

        return await self._client.delete(
            url=url,
            auth=auth,
            headers=headers,
            params=params
        )
    
    async def options(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params
        )

        return await self._client.options(
            url,
            auth=auth,
            headers=headers,
            params=params
        )
    
    async def head(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url,
            auth=auth,
            headers=headers,
            params=params
        )

        return await self._client.head(
            url,
            auth=auth,
            headers=headers,
            params=params
        )
    
    async def close(self):
        if self._client:
            await self._client.close()

    def abort(self):
        if self._client:
            asyncio.create_task(self._client.close())