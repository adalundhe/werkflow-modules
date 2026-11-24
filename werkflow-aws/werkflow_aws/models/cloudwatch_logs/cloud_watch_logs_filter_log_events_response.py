from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_filtered_log_event import CloudWatchLogsFilteredLogEvent
from .cloud_watch_logs_searched_log_stream import CloudWatchLogsSearchedLogStream


class CloudWatchLogsFilterLogEventsResponse(BaseModel):
    events: list[CloudWatchLogsFilteredLogEvent] | None = None
    searchedLogStreams: list[CloudWatchLogsSearchedLogStream] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
