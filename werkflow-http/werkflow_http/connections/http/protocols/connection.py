from __future__ import annotations

import asyncio
from ssl import SSLContext
from typing import Dict, Optional, Tuple

from werkflow_http.connections.http.models.http.types import SocketConfig
from .shared import (
    Reader,
    Writer,
    _DEFAULT_LIMIT,
)
from .tcp import TCPConnection

PoolKey = Tuple[str, int, bool]


class HTTPConnection:

    __slots__ = (
        'dns_address',
        'port',
        'ssl',
        'ip_addr',
        'lock',
        'reader',
        'writer',
        'connected',
        'reset_connection',
        'pending',
        '_reader_and_writer',
    )

    def __init__(self, reset_connection: bool = False) -> None:
        self.dns_address: Optional[str] = None
        self.port: Optional[int] = None
        self.ssl: Optional[SSLContext] = None
        self.ip_addr: Optional[str] = None
        self.lock = asyncio.Lock()

        self.reader: Optional[Reader] = None
        self.writer: Optional[Writer] = None

        self._reader_and_writer: Dict[
            PoolKey,
            Tuple[Reader, Writer, TCPConnection],
        ] = {}

        self.connected: bool = False
        self.reset_connection: bool = reset_connection
        self.pending: int = 0

    @staticmethod
    def _is_connection_reusable(reader: Reader, writer: Writer) -> bool:
        if writer.is_closing():
            return False
        if reader.at_eof() or reader._eof:
            return False
        if reader.exception() is not None:
            return False
        return True

    async def make_connection(
        self,
        hostname: str,
        dns_address: str,
        port: int,
        socket_config: SocketConfig,
        ssl: Optional[SSLContext] = None,
        timeout: Optional[float] = None,
        ssl_upgrade: bool = False,
    ) -> None:
        pool_key: PoolKey = (hostname, port, ssl is not None)
        existing = self._reader_and_writer.get(pool_key)

        if (
            existing is not None
            and not ssl_upgrade
            and not self.reset_connection
            and self._is_connection_reusable(existing[0], existing[1])
        ):
            reader, writer, _ = existing
            self.reader = reader
            self.writer = writer
            self.dns_address = dns_address
            self.port = port
            self.ssl = ssl
            self.connected = True
            return

        if existing is not None:
            _, _, old_tcp = existing
            await old_tcp.close()
            self._reader_and_writer.pop(pool_key, None)

        tcp_connection = TCPConnection()
        reader, writer = await tcp_connection.create(
            hostname,
            socket_config,
            ssl=ssl,
        )

        self.reader = reader
        self.writer = writer
        self._reader_and_writer[pool_key] = (reader, writer, tcp_connection)
        self.dns_address = dns_address
        self.port = port
        self.ssl = ssl
        self.connected = True

    @property
    def empty(self) -> bool:
        return self.reader is None or not self.reader._buffer

    async def read(self) -> bytes:
        assert self.reader is not None
        return await self.reader.read(n=_DEFAULT_LIMIT)

    async def readexactly(self, n_bytes: int) -> bytes:
        assert self.reader is not None
        return await self.reader.readexactly(n=n_bytes)

    async def readuntil(self, sep: bytes = b'\n') -> bytes:
        assert self.reader is not None
        return await self.reader.readuntil(separator=sep)

    async def readline(self) -> bytes:
        assert self.reader is not None
        return await self.reader.readline()

    def write(self, data: bytes | bytearray | memoryview) -> None:
        assert self.writer is not None
        self.writer.write(data)

    def reset_buffer(self) -> None:
        if self.reader is not None:
            self.reader._buffer = bytearray()

    async def read_headers(self) -> Dict[bytes, bytes]:
        assert self.reader is not None
        return await self.reader.read_headers()

    def abort(self) -> None:
        entries = list(self._reader_and_writer.values())
        self._reader_and_writer.clear()
        self.reader = None
        self.writer = None
        self.connected = False
        for _, _, tcp_conn in entries:
            try:
                tcp_conn.abort()
            except Exception:
                pass

    async def close(self) -> None:
        self.abort()
