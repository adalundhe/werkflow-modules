import asyncio
from asyncio import (
    AbstractEventLoop,
    Future,
    Protocol,
    get_event_loop,
)
from typing import Any, Optional


class FlowControlMixin(Protocol):
    """Reusable flow control logic for StreamWriter.drain().
    This implements the protocol methods pause_writing(),
    resume_writing() and connection_lost().  If the subclass overrides
    these it must call the super methods.
    StreamWriter.drain() must wait for _drain_helper() coroutine.
    """
    __slots__ = (
        '_loop',
        '_paused',
        '_drain_waiter',
        '_connection_lost',
    )

    def __init__(self, loop: Optional[AbstractEventLoop] = None) -> None:
        if loop is not None:
            self._loop: AbstractEventLoop = loop
        else:
            try:
                self._loop = asyncio.get_running_loop()
            except RuntimeError:
                self._loop = get_event_loop()

        self._paused: bool = False
        self._drain_waiter: Optional[Future[None]] = None
        self._connection_lost: bool = False

    def pause_writing(self) -> None:
        assert not self._paused
        self._paused = True

    def resume_writing(self) -> None:
        assert self._paused
        self._paused = False

        waiter = self._drain_waiter
        if waiter is not None:
            self._drain_waiter = None
            if not waiter.done():
                waiter.set_result(None)

    def connection_lost(self, exc: Optional[BaseException]) -> None:
        self._connection_lost = True
        # Wake up the writer if currently paused.
        if not self._paused:
            return
        waiter = self._drain_waiter
        if waiter is None:
            return
        self._drain_waiter = None
        if waiter.done():
            return
        if exc is None:
            waiter.set_result(None)
        else:
            waiter.set_exception(exc)

    async def _drain_helper(self) -> None:
        if self._connection_lost:
            raise ConnectionResetError('Connection lost')
        if not self._paused:
            return
        waiter = self._drain_waiter
        assert waiter is None or waiter.cancelled()
        waiter = self._loop.create_future()
        self._drain_waiter = waiter
        await waiter

    def _get_close_waiter(self, stream: Any) -> Future[None]:
        raise NotImplementedError
