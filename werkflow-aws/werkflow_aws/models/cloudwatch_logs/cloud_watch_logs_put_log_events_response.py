from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_rejected_entity_info import CloudWatchLogsRejectedEntityInfo
from .cloud_watch_logs_rejected_log_events_info import CloudWatchLogsRejectedLogEventsInfo


class CloudWatchLogsPutLogEventsResponse(BaseModel):
    nextSequenceToken: StrictStr | None = None
    rejectedLogEventsInfo: CloudWatchLogsRejectedLogEventsInfo | None = None
    rejectedEntityInfo: CloudWatchLogsRejectedEntityInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
