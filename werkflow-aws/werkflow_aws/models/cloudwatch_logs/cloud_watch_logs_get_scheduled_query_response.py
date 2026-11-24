from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_destination_configuration import CloudWatchLogsDestinationConfiguration


class CloudWatchLogsGetScheduledQueryResponse(BaseModel):
    scheduledQueryArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    queryLanguage: StrictStr | None = None
    queryString: StrictStr | None = None
    logGroupIdentifiers: list[StrictStr] | None = None
    scheduleExpression: StrictStr | None = None
    timezone: StrictStr | None = None
    startTimeOffset: StrictInt | None = None
    endTimeOffset: StrictInt | None = None
    destinationConfiguration: CloudWatchLogsDestinationConfiguration | None = None
    state: StrictStr | None = None
    scheduleType: StrictStr | None = None
    lastTriggeredTime: StrictInt | None = None
    lastExecutionStatus: StrictStr | None = None
    scheduleStartTime: StrictInt | None = None
    scheduleEndTime: StrictInt | None = None
    executionRoleArn: StrictStr | None = None
    creationTime: StrictInt | None = None
    lastUpdatedTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
