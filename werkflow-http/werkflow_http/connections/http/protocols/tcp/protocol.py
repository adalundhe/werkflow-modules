from __future__ import annotations

import asyncio
import inspect
from asyncio import (
    AbstractEventLoop,
    BaseTransport,
    Future,
    Protocol,
    Transport,
)
from typing import Any, Callable, Optional
from weakref import ReferenceType, ref

from werkflow_http.connections.http.protocols.shared import (
    FlowControlMixin,
    Reader,
    Writer,
)


class TCPProtocol(FlowControlMixin, Protocol):
    """Helper class to adapt between Protocol and StreamReader."""

    __slots__ = (
        '_source_traceback',
        '_reject_connection',
        '_stream_writer',
        '_transport',
        '_client_connected_cb',
        '_over_ssl',
        '_closed',
        '_stream_reader_wr',
        '_strong_reader',
    )

    def __init__(
        self,
        stream_reader: Optional[Reader],
        client_connected_cb: Optional[Callable[..., Any]] = None,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        super().__init__(loop=loop)
        self._source_traceback: Any = None

        if stream_reader is not None:
            self._stream_reader_wr: Optional[ReferenceType[Reader]] = ref(stream_reader)
            self._source_traceback = stream_reader._source_traceback
        else:
            self._stream_reader_wr = None

        if client_connected_cb is not None:
            self._strong_reader: Optional[Reader] = stream_reader
        else:
            self._strong_reader = None

        self._reject_connection: bool = False
        self._stream_writer: Optional[Writer] = None
        self._transport: Optional[Transport] = None
        self._client_connected_cb = client_connected_cb
        self._over_ssl: bool = False
        self._closed: Future[None] = self._loop.create_future()

    @property
    def _stream_reader(self) -> Optional[Reader]:
        if self._stream_reader_wr is None:
            return None
        return self._stream_reader_wr()

    def _replace_writer(self, writer: Writer) -> None:
        transport = writer.transport
        self._stream_writer = writer
        if isinstance(transport, Transport):
            self._transport = transport
        self._over_ssl = transport.get_extra_info('sslcontext') is not None

    def connection_made(self, transport: BaseTransport) -> None:
        assert isinstance(transport, Transport)
        if self._reject_connection:
            context: dict[str, Any] = {
                'message': (
                    'An open stream was garbage collected prior to '
                    'establishing network connection; '
                    'call "stream.close()" explicitly.'
                )
            }
            if self._source_traceback:
                context['source_traceback'] = self._source_traceback
            self._loop.call_exception_handler(context)
            transport.abort()
            return
        self._transport = transport
        reader = self._stream_reader
        if reader is not None:
            reader.set_transport(transport)
        self._over_ssl = transport.get_extra_info('sslcontext') is not None
        if self._client_connected_cb is not None:
            self._stream_writer = Writer(
                transport,
                self,
                reader,
                self._loop,
            )
            res = self._client_connected_cb(reader, self._stream_writer)
            if inspect.iscoroutine(res):
                self._loop.create_task(res)
            self._strong_reader = None

    def connection_lost(self, exc: Optional[BaseException]) -> None:
        reader = self._stream_reader
        if reader is not None:
            if exc is None:
                reader.feed_eof()
            else:
                reader.set_exception(exc)
        if not self._closed.done():
            if exc is None:
                self._closed.set_result(None)
            else:
                self._closed.set_exception(exc)
        super().connection_lost(exc)
        self._stream_reader_wr = None
        self._stream_writer = None
        self._transport = None

    def data_received(self, data: bytes) -> None:
        reader = self._stream_reader
        if reader is not None:
            reader.feed_data(data)

    def eof_received(self) -> bool:
        reader = self._stream_reader
        if reader is not None:
            reader.feed_eof()
        if self._over_ssl:
            return False
        return True

    def _get_close_waiter(self, stream: Any) -> Future[None]:
        return self._closed

    def __del__(self) -> None:
        try:
            closed = self._closed
        except AttributeError:
            pass
        else:
            if closed.done() and not closed.cancelled():
                closed.exception()
