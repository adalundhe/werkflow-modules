from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_output_log_event import CloudWatchLogsOutputLogEvent


class CloudWatchLogsGetLogEventsResponse(BaseModel):
    events: list[CloudWatchLogsOutputLogEvent] | None = None
    nextForwardToken: StrictStr | None = None
    nextBackwardToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
