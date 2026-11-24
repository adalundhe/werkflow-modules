import asyncio
import socket
from ssl import SSLContext
from typing import Optional, Tuple

from werkflow_http.connections.http.models.http.types import SocketConfig
from werkflow_http.connections.http.protocols.shared import (
    Reader,
    Writer,
    _DEFAULT_LIMIT,
)
from .protocol import TCPProtocol


class TCPConnection:

    def __init__(self) -> None:
        self.loop: Optional[asyncio.AbstractEventLoop] = None
        self.transport: Optional[asyncio.Transport] = None
        self._connection: Optional[TCPProtocol] = None
        self.socket: Optional[socket.socket] = None
        self._writer: Optional[Writer] = None

    async def create(
        self,
        hostname: Optional[str] = None,
        socket_config: Optional[SocketConfig] = None,
        *,
        limit: int = _DEFAULT_LIMIT,
        ssl: Optional[SSLContext] = None,
    ) -> Tuple[Reader, Writer]:
        if socket_config is None:
            raise ValueError('socket_config is required to create a TCP connection')

        loop = asyncio.get_running_loop()
        self.loop = loop

        family, type_, proto, _, address = socket_config
        socket_family = socket.AF_INET if family == socket.AF_INET else socket.AF_INET6

        sock = socket.socket(family=socket_family, type=type_, proto=proto)
        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            await loop.run_in_executor(None, sock.connect, address)
            sock.setblocking(False)

            reader = Reader(limit=limit, loop=loop)
            reader_protocol = TCPProtocol(reader, loop=loop)

            server_hostname = hostname if ssl is not None else None

            transport, _ = await loop.create_connection(
                lambda: reader_protocol,
                sock=sock,
                family=socket_family,
                server_hostname=server_hostname,
                ssl=ssl,
            )
        except Exception:
            try:
                sock.close()
            except Exception:
                pass
            raise

        self.socket = sock
        self.transport = transport
        self._connection = reader_protocol
        self._writer = Writer(transport, reader_protocol, reader, loop)

        return reader, self._writer

    def abort(self) -> None:
        transport = self.transport
        self.transport = None
        self._writer = None
        self._connection = None
        if transport is not None:
            ssl_protocol = getattr(transport, '_ssl_protocol', None)
            if ssl_protocol is not None:
                try:
                    ssl_protocol.pause_writing()
                except Exception:
                    pass
            try:
                transport.close()
            except Exception:
                pass

    async def close(self) -> None:
        self.abort()
