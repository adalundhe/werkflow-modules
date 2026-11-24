from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_start_live_tail_response_stream import CloudWatchLogsStartLiveTailResponseStream


class CloudWatchLogsStartLiveTailResponse(BaseModel):
    responseStream: CloudWatchLogsStartLiveTailResponseStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
