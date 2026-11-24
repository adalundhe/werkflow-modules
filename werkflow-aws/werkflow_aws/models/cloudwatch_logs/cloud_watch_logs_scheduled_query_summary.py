from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_destination_configuration import CloudWatchLogsDestinationConfiguration


class CloudWatchLogsScheduledQuerySummary(BaseModel):
    scheduledQueryArn: StrictStr | None = None
    name: StrictStr | None = None
    state: StrictStr | None = None
    scheduleType: StrictStr | None = None
    lastTriggeredTime: StrictInt | None = None
    lastExecutionStatus: StrictStr | None = None
    scheduleExpression: StrictStr | None = None
    timezone: StrictStr | None = None
    destinationConfiguration: CloudWatchLogsDestinationConfiguration | None = None
    creationTime: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
