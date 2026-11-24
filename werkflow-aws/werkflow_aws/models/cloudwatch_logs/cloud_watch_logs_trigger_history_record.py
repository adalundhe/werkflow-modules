from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_scheduled_query_destination import CloudWatchLogsScheduledQueryDestination


class CloudWatchLogsTriggerHistoryRecord(BaseModel):
    queryId: StrictStr | None = None
    executionStatus: StrictStr | None = None
    triggeredTimestamp: StrictInt | None = None
    errorMessage: StrictStr | None = None
    destinations: list[CloudWatchLogsScheduledQueryDestination] | None = None
