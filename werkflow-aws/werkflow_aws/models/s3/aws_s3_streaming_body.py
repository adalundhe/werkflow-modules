import asyncio
from botocore.response import StreamingBody


class AWSs3StreamingBody:

    def __init__(
        self,
        body: StreamingBody
    ) -> None:
        self.body = body

    async def read(self):
        return await asyncio.to_thread(
            self.body.read
        )
    
    async def readable(self):
        return await asyncio.to_thread(
            self.body.readable
        )
    
    async def readlines(self):
        return await asyncio.to_thread(
            self.body.readline
        )
    
    async def __aiter__(self):
        for chunk in (
            await asyncio.to_thread(
                self.body.__iter__
            )
        ):
            yield chunk

    async def __anext__(self):
        return await asyncio.to_thread(
            self.body.__next__
        )
    
    async def __aexit__(self):
        return await asyncio.to_thread(
            self.body.__aexit__
        )
    
    async def __aenter__(self):
        return await asyncio.to_thread(
            self.body.__enter__
        )
    
    def iter_lines(
        self,
        chunk_size: int=1024,
        keepends: bool=False
    ):
        return asyncio.to_thread(
            self.body.iter_lines,
            chunk_size=chunk_size,
            keepends=keepends
        )
    
    def iter_chunks(
        self,
        chunk_size: int=1024
    ):
        return asyncio.to_thread(
            self.body.iter_chunks,
            chunk_size=chunk_size
        )
    
    async def tell(self):
        return await asyncio.to_thread(
            self.body.tell
        )
    
    async def close(self):
        return await asyncio.to_thread(
            self.body.close
        )