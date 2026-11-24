import asyncio
from collections.abc import Sequence
from typing import Any, Dict

import orjson
from pydantic import BaseModel
from werkflow_core import Module

from .connections.http import MercurySyncHTTPConnection
from .connections.http.models.http import (
    File as HTTPFile,
    HTTPResponse,
)
from .request import (
    Data,
    File,
    Headers,
    Params,
    Request,
    RequestWithData,
)


class HTTP(Module):
    module_enabled = True
    dependencies = [
        'aiodns',
        'orjson',
        'pydantic',
    ]

    def __init__(self, verify_ssl: bool = True) -> None:
        super().__init__()
        self._verify_ssl = verify_ssl
        self._client: MercurySyncHTTPConnection | None = None

    def _get_client(self) -> MercurySyncHTTPConnection:
        if self._client is None:
            self._client = MercurySyncHTTPConnection(verify_ssl=self._verify_ssl)
        return self._client

    @staticmethod
    def _normalize_files(
        files: Sequence[File | str | Dict[str, Any]] | None,
    ) -> list[File | str] | None:
        if not files:
            return None

        return [
            HTTPFile(**file) if isinstance(file, dict) else file
            for file in files
        ]

    @staticmethod
    def _is_json_content_type(headers: Headers | None) -> bool:
        if not headers:
            return False

        for header_key, header_value in headers.items():
            if header_key.lower() == 'content-type' and header_value is not None:
                value_str = (
                    header_value.decode('utf-8', errors='replace')
                    if isinstance(header_value, bytes)
                    else str(header_value)
                )
                media_type = value_str.split(';', 1)[0].strip().lower()
                return media_type == 'application/json'

        return False

    @classmethod
    def _encode_data(
        cls,
        headers: Headers | None,
        data: Data,
    ) -> Data:
        if data is None:
            return None

        if cls._is_json_content_type(headers):
            if isinstance(data, bytes):
                return data
            if isinstance(data, str):
                return data.encode('utf-8')
            if isinstance(data, BaseModel):
                return orjson.dumps(data.model_dump(mode='json', exclude_none=True))
            return orjson.dumps(data)

        return data

    async def get(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
    ) -> HTTPResponse:
        client = self._get_client()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
        )

        return await client.get(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
        )

    async def post(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
        data: Data = None,
        files: Sequence[File | str | Dict[str, Any]] | None = None,
    ) -> HTTPResponse:
        client = self._get_client()
        normalized_files = self._normalize_files(files)

        RequestWithData(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
            data=data,
            files=normalized_files,
        )

        encoded_data = self._encode_data(headers, data)

        return await client.post(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
            data=encoded_data,
            files=normalized_files,
        )

    async def put(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
        data: Data = None,
        files: Sequence[File | str | Dict[str, Any]] | None = None,
    ) -> HTTPResponse:
        client = self._get_client()
        normalized_files = self._normalize_files(files)

        RequestWithData(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
            data=data,
            files=normalized_files,
        )

        encoded_data = self._encode_data(headers, data)

        return await client.put(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
            data=encoded_data,
            files=normalized_files,
        )

    async def patch(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
        data: Data = None,
        files: Sequence[File | str | Dict[str, Any]] | None = None,
    ) -> HTTPResponse:
        client = self._get_client()
        normalized_files = self._normalize_files(files)

        RequestWithData(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
            data=data,
            files=normalized_files,
        )

        encoded_data = self._encode_data(headers, data)

        return await client.patch(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
            data=encoded_data,
            files=normalized_files,
        )

    async def delete(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
    ) -> HTTPResponse:
        client = self._get_client()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
        )

        return await client.delete(
            url=url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
        )

    async def options(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
    ) -> HTTPResponse:
        client = self._get_client()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
        )

        return await client.options(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
        )

    async def head(
        self,
        url: str,
        auth: tuple[str, str] | None = None,
        headers: Headers | None = None,
        params: Params | None = None,
    ) -> HTTPResponse:
        client = self._get_client()

        Request(
            url=url,
            auth=auth,
            headers=headers,
            params=params,
        )

        return await client.head(
            url,
            auth=auth,
            headers=dict(headers) if headers is not None else None,
            params=dict(params) if params is not None else None,
        )

    async def close(self) -> None:
        if self._client is not None:
            client = self._client
            self._client = None
            await client.close()

    def abort(self) -> None:
        if self._client is not None:
            client = self._client
            self._client = None
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                client.abort()
                return
            loop.create_task(client.close())
