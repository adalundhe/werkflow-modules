import asyncio
from collections.abc import AsyncIterator, Iterator
from typing import Any, Self
from botocore.response import StreamingBody


class AWSS3StreamingBody:

    def __init__(self, body: StreamingBody) -> None:
        self.body = body
        self._iter: Iterator[bytes] | None = None

    async def read(self, amt: int | None = None) -> bytes:
        return await asyncio.to_thread(self.body.read, amt)

    async def readable(self) -> bool:
        return await asyncio.to_thread(self.body.readable)

    async def readlines(self) -> list[bytes]:
        return await asyncio.to_thread(self.body.readlines)

    def __aiter__(self) -> Self:
        self._iter = iter(self.body)
        return self

    async def __anext__(self) -> bytes:
        if self._iter is None:
            self._iter = iter(self.body)

        iterator = self._iter

        def _next_chunk() -> tuple[bool, bytes]:
            try:
                return True, next(iterator)
            except StopIteration:
                return False, b''

        has_item, chunk = await asyncio.to_thread(_next_chunk)
        if not has_item:
            raise StopAsyncIteration()
        return chunk

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: Any,
        exc_val: Any,
        exc_tb: Any,
    ) -> None:
        await self.close()

    async def iter_lines(
        self,
        chunk_size: int = 1024,
        keepends: bool = False,
    ) -> AsyncIterator[bytes]:
        iterator = self.body.iter_lines(chunk_size=chunk_size, keepends=keepends)

        def _next() -> tuple[bool, bytes]:
            try:
                return True, next(iterator)
            except StopIteration:
                return False, b''

        while True:
            has_item, line = await asyncio.to_thread(_next)
            if not has_item:
                break
            yield line

    async def iter_chunks(
        self,
        chunk_size: int = 1024,
    ) -> AsyncIterator[bytes]:
        iterator = self.body.iter_chunks(chunk_size=chunk_size)

        def _next() -> tuple[bool, bytes]:
            try:
                return True, next(iterator)
            except StopIteration:
                return False, b''

        while True:
            has_item, chunk = await asyncio.to_thread(_next)
            if not has_item:
                break
            yield chunk

    async def tell(self) -> int:
        return await asyncio.to_thread(self.body.tell)

    async def close(self) -> None:
        await asyncio.to_thread(self.body.close)
