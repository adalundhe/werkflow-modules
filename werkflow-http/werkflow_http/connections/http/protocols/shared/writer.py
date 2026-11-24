import asyncio
from asyncio import (
    DatagramTransport,
    Transport,
    sleep,
)
from typing import Any, Iterable, Optional, Union


class Writer:
    __slots__ = (
        '_transport',
        '_protocol',
        '_reader',
        '_loop',
        '_complete_fut',
    )
    """Wraps a Transport.
    This exposes write(), writelines(), [can_]write_eof(),
    get_extra_info() and close().  It adds drain() which returns an
    optional Future on which you can wait for flow control.  It also
    adds a transport property which references the Transport
    directly.
    """

    def __init__(
        self,
        transport: Union[Transport, DatagramTransport],
        protocol: Any,
        reader: Any,
        loop: asyncio.AbstractEventLoop,
    ) -> None:
        self._transport: Union[Transport, DatagramTransport] = transport
        self._protocol: Any = protocol
        self._reader: Any = reader
        self._loop: asyncio.AbstractEventLoop = loop
        self._complete_fut: asyncio.Future[None] = self._loop.create_future()
        self._complete_fut.set_result(None)

    def __repr__(self) -> str:
        info = [self.__class__.__name__, f'transport={self._transport!r}']
        if self._reader is not None:
            info.append(f'reader={self._reader!r}')
        return '<{}>'.format(' '.join(info))

    @property
    def transport(self) -> Union[Transport, DatagramTransport]:
        return self._transport

    def write(self, data: Union[bytes, bytearray, memoryview]) -> None:
        assert isinstance(self._transport, Transport)
        self._transport.write(data)

    def send(self, data: bytes) -> None:
        assert isinstance(self._transport, DatagramTransport)
        self._transport.sendto(data)

    def writelines(self, data: Iterable[Union[bytes, bytearray, memoryview]]) -> None:
        assert isinstance(self._transport, Transport)
        self._transport.writelines(data)

    def write_eof(self) -> None:
        assert isinstance(self._transport, Transport)
        self._transport.write_eof()

    def can_write_eof(self) -> bool:
        assert isinstance(self._transport, Transport)
        return self._transport.can_write_eof()

    def close(self) -> None:
        self._transport.close()

    def is_closing(self) -> bool:
        return self._transport.is_closing()

    async def wait_closed(self) -> None:
        await self._protocol._get_close_waiter(self)

    def get_extra_info(self, name: str, default: Any = None) -> Any:
        return self._transport.get_extra_info(name, default)

    async def drain(self) -> None:
        """Flush the write buffer."""
        if self._reader is not None:
            exc = self._reader.exception()
            if exc is not None:
                raise exc
        if self._transport.is_closing():
            await sleep(0)
        await self._protocol._drain_helper()

    async def start_tls(
        self,
        sslcontext: Any,
        *,
        server_hostname: Optional[str] = None,
        ssl_handshake_timeout: Optional[float] = None,
    ) -> None:
        server_side = self._protocol._client_connected_cb is not None
        protocol = self._protocol

        await self.drain()

        assert isinstance(self._transport, Transport)
        new_transport = await self._loop.start_tls(
            self._transport,
            protocol,
            sslcontext,
            server_side=server_side,
            server_hostname=server_hostname,
            ssl_handshake_timeout=ssl_handshake_timeout,
        )

        if new_transport is not None:
            self._transport = new_transport
        protocol._replace_writer(self)
