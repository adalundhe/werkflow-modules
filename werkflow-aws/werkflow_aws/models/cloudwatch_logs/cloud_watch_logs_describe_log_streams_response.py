from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_log_stream import CloudWatchLogsLogStream


class CloudWatchLogsDescribeLogStreamsResponse(BaseModel):
    logStreams: list[CloudWatchLogsLogStream] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
