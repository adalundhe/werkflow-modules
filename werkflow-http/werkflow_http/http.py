import asyncio

import orjson
from werkflow.modules.base import Module

from werkflow_http.connections.http import MercurySyncHTTPConnection

from .request import Data, Headers, Params, Request, RequestWithData


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
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            headers=headers,
            params=params
        )

        return await self._client.get(
            url,
            headers=headers,
            params=params
        )
    
    async def post(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url=url,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers = {
            header_key.lower(): header_value for header_key, header_value in headers.items()
        }

        if lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data)

        return await self._client.post(
            url,
            headers=headers,
            params=params,
            data=data
        )
    
    async def put(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url=url,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers = {
            header_key.lower(): header_value for header_key, header_value in headers.items()
        }

        if lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data).decode()

        return await self._client.put(
            url,
            headers=headers,
            params=params,
            data=data
        )
    
    async def patch(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None,
        data: Data=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        RequestWithData(
            url,
            headers=headers,
            params=params,
            data=data
        )

        lowered_headers = {
            header_key.lower(): header_value for header_key, header_value in headers.items()
        }

        if lowered_headers.get('content-type') == 'application/json':
            data = orjson.dumps(data).decode()

        return await self._client.patch(
            url,
            headers=headers,
            params=params,
            data=data
        )
    
    async def delete(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            headers=headers,
            params=params
        )

        return await self._client.delete(
            url=url,
            headers=headers,
            params=params
        )
    
    async def options(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url=url,
            headers=headers,
            params=params
        )

        return await self._client.options(
            url,
            headers=headers,
            params=params
        )
    
    async def head(
        self,
        url: str,
        headers: Headers=None,
        params: Params=None
    ):
        if self._client is None:
            self._client = MercurySyncHTTPConnection()

        Request(
            url,
            headers=headers,
            params=params
        )

        return await self._client.head(
            url,
            headers=headers,
            params=params
        )
    
    async def close(self):
        if self._client:
            await self._client.close()

    def abort(self):
        if self._client:
            asyncio.create_task(self._client.close())