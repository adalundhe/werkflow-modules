from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_entity import CloudWatchLogsEntity
from .cloud_watch_logs_input_log_event import CloudWatchLogsInputLogEvent


class CloudWatchLogsPutLogEventsRequest(BaseModel):
    logGroupName: StrictStr
    logStreamName: StrictStr
    logEvents: list[CloudWatchLogsInputLogEvent]
    sequenceToken: StrictStr | None = None
    entity: CloudWatchLogsEntity | None = None
