import asyncio
from asyncio import (
    AbstractEventLoop,
    Future,
    ReadTransport,
    Transport,
    get_event_loop,
)
from asyncio.exceptions import LimitOverrunError
from typing import AsyncIterator, Dict, Optional, Tuple

from .constants import _DEFAULT_LIMIT


class Reader:

    _source_traceback = None
    __slots__ = (
        '_limit',
        '_loop',
        '_buffer',
        '_eof',
        '_waiter',
        '_exception',
        '_transport',
        '_paused',
        '__weakref__',
    )

    def __init__(
        self,
        limit: int = _DEFAULT_LIMIT,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        if limit <= 0:
            raise ValueError('Limit cannot be <= 0')

        self._limit = limit
        if loop is not None:
            self._loop: AbstractEventLoop = loop
        else:
            try:
                self._loop = asyncio.get_running_loop()
            except RuntimeError:
                self._loop = get_event_loop()

        self._buffer = bytearray()
        self._eof = False
        self._waiter: Optional[Future[None]] = None
        self._exception: Optional[BaseException] = None
        self._transport: Optional[Transport] = None
        self._paused = False

    def exception(self) -> Optional[BaseException]:
        return self._exception

    def set_exception(self, exc: BaseException) -> None:
        self._exception = exc

        waiter = self._waiter
        if waiter is not None:
            self._waiter = None
            if not waiter.done():
                waiter.set_exception(exc)

    def set_transport(self, transport: Transport) -> None:
        self._transport = transport

    def _maybe_resume_transport(self) -> None:
        if self._paused and len(self._buffer) <= self._limit:
            self._paused = False
            if isinstance(self._transport, ReadTransport):
                self._transport.resume_reading()

    def feed_eof(self) -> None:
        self._eof = True

        waiter = self._waiter
        if waiter is not None:
            self._waiter = None
            if not waiter.done():
                waiter.set_result(None)

    def at_eof(self) -> bool:
        """Return True if the buffer is empty and 'feed_eof' was called."""
        return self._eof and not self._buffer

    def feed_data(self, data: bytes) -> None:
        assert not self._eof, 'feed_data after feed_eof'

        if not data:
            return

        self._buffer.extend(data)

        waiter = self._waiter
        if waiter is not None:
            self._waiter = None
            if not waiter.done():
                waiter.set_result(None)

        if (
            self._transport is not None
            and not self._paused
            and len(self._buffer) > 2 * self._limit
        ):
            try:
                if isinstance(self._transport, ReadTransport):
                    self._transport.pause_reading()
            except NotImplementedError:
                self._transport = None
            else:
                self._paused = True

    async def _wait_for_data(self, func_name: str) -> None:
        """Wait until feed_data() or feed_eof() is called.
        If stream was paused, automatically resume it.
        """
        if self._waiter is not None:
            raise RuntimeError(
                f'{func_name}() called while another coroutine is '
                f'already waiting for incoming data'
            )

        assert not self._eof, '_wait_for_data after EOF'

        if self._paused:
            self._paused = False
            if isinstance(self._transport, ReadTransport):
                self._transport.resume_reading()

        self._waiter = self._loop.create_future()
        try:
            await self._waiter
        finally:
            self._waiter = None

    async def read(self, n: int = -1) -> bytes:
        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        if n < 0:
            blocks = []
            while True:
                block = await self.read(self._limit)
                if not block:
                    break
                blocks.append(block)
            return b''.join(blocks)

        if not self._buffer and not self._eof:
            await self._wait_for_data('read')

        data = bytes(self._buffer[:n])
        del self._buffer[:n]

        self._maybe_resume_transport()
        return data

    async def readline_fast(self, sep: bytes = b'\n') -> bytes:
        try:
            return await self.readuntil(sep)
        except asyncio.IncompleteReadError as e:
            return e.partial

    async def readline(self) -> bytes:
        sep = b'\n'
        seplen = len(sep)
        try:
            line = await self.readuntil(sep)
        except asyncio.IncompleteReadError as e:
            return e.partial
        except asyncio.LimitOverrunError as e:
            if self._buffer.startswith(sep, e.consumed):
                del self._buffer[:e.consumed + seplen]
            else:
                self._buffer.clear()
            self._maybe_resume_transport()
            raise ValueError(e.args[0])
        return line

    async def readuntil(self, separator: bytes = b'\n') -> bytes:
        """Read data from the stream until ``separator`` is found."""
        seplen = len(separator)
        if seplen == 0:
            raise ValueError('Separator should be at least one-byte string')

        if self._exception is not None:
            raise self._exception

        offset = 0

        while True:
            buflen = len(self._buffer)

            if buflen - offset >= seplen:
                isep = self._buffer.find(separator, offset)

                if isep != -1:
                    break

                offset = buflen + 1 - seplen
                if offset > self._limit:
                    raise LimitOverrunError(
                        'Separator is not found, and chunk exceed the limit',
                        offset,
                    )

            if self._eof:
                chunk = bytes(self._buffer)
                self._buffer.clear()
                raise asyncio.IncompleteReadError(chunk, None)

            await self._wait_for_data('readuntil')

        if isep > self._limit:
            raise LimitOverrunError(
                'Separator is found, but chunk is longer than limit',
                isep,
            )

        chunk = bytes(self._buffer[:isep + seplen])
        del self._buffer[:isep + seplen]
        self._maybe_resume_transport()
        return chunk

    async def read_headers(self, separator: bytes = b'\n') -> Dict[bytes, bytes]:
        headers: Dict[bytes, bytes] = {}
        async for key, value, _ in self.iter_headers(separator=separator):
            key_lower = key.lower()
            if key_lower == b'set-cookie' and key_lower in headers:
                headers[key_lower] = headers[key_lower] + b'; ' + value.strip()
            else:
                headers[key_lower] = value.strip()

        return headers

    async def readexactly(self, n: int) -> bytes:
        """Read exactly `n` bytes."""
        if n < 0:
            raise ValueError('readexactly size can not be less than zero')

        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        while len(self._buffer) < n:
            if self._eof:
                incomplete = bytes(self._buffer)
                self._buffer.clear()
                raise asyncio.IncompleteReadError(incomplete, n)

            await self._wait_for_data('readexactly')

        if len(self._buffer) == n:
            data = bytes(self._buffer)
            self._buffer.clear()
        else:
            data = bytes(memoryview(self._buffer)[:n])
            del self._buffer[:n]
        self._maybe_resume_transport()
        return data

    async def iter_headers(
        self,
        separator: bytes = b'\n',
    ) -> AsyncIterator[Tuple[bytes, bytes, bytes]]:
        while True:
            if self._exception is not None:
                raise self._exception

            try:
                chunk = await self.readuntil(separator)
            except asyncio.IncompleteReadError as e:
                chunk = e.partial
                if not chunk:
                    break

            stripped = chunk.strip()
            if not stripped or b':' not in stripped:
                break

            key, value = stripped.split(b':', 1)
            yield key.strip().lower(), value.strip(), chunk

    def __aiter__(self) -> 'Reader':
        return self

    async def __anext__(self) -> bytes:
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val
