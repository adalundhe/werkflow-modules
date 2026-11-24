from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_destination_configuration import CloudWatchLogsDestinationConfiguration


class CloudWatchLogsCreateScheduledQueryRequest(BaseModel):
    name: StrictStr
    queryLanguage: Literal['CWLI', 'SQL', 'PPL']
    queryString: StrictStr
    scheduleExpression: StrictStr
    executionRoleArn: StrictStr
    description: StrictStr | None = None
    logGroupIdentifiers: list[StrictStr] | None = None
    timezone: StrictStr | None = None
    startTimeOffset: StrictInt | None = None
    endTimeOffset: StrictInt | None = None
    destinationConfiguration: CloudWatchLogsDestinationConfiguration | None = None
    scheduleStartTime: StrictInt | None = None
    scheduleEndTime: StrictInt | None = None
    state: Literal['ENABLED', 'DISABLED'] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
