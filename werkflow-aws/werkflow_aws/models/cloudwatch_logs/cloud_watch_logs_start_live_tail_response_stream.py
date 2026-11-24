from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_live_tail_session_start import CloudWatchLogsLiveTailSessionStart
from .cloud_watch_logs_live_tail_session_update import CloudWatchLogsLiveTailSessionUpdate
from .cloud_watch_logs_session_streaming_exception import CloudWatchLogsSessionStreamingException
from .cloud_watch_logs_session_timeout_exception import CloudWatchLogsSessionTimeoutException


class CloudWatchLogsStartLiveTailResponseStream(BaseModel):
    sessionStart: CloudWatchLogsLiveTailSessionStart | None = None
    sessionUpdate: CloudWatchLogsLiveTailSessionUpdate | None = None
    SessionTimeoutException: CloudWatchLogsSessionTimeoutException | None = None
    SessionStreamingException: CloudWatchLogsSessionStreamingException | None = None
