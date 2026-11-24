from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_live_tail_session_log_event import CloudWatchLogsLiveTailSessionLogEvent
from .cloud_watch_logs_live_tail_session_metadata import CloudWatchLogsLiveTailSessionMetadata


class CloudWatchLogsLiveTailSessionUpdate(BaseModel):
    sessionMetadata: CloudWatchLogsLiveTailSessionMetadata | None = None
    sessionResults: list[CloudWatchLogsLiveTailSessionLogEvent] | None = None
