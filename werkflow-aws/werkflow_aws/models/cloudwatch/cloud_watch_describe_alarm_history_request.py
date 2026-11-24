from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchDescribeAlarmHistoryRequest(BaseModel):
    AlarmName: StrictStr | None = None
    AlarmContributorId: StrictStr | None = None
    AlarmTypes: list[Literal['CompositeAlarm', 'MetricAlarm', 'LogAlarm']] | None = None
    HistoryItemType: Literal['ConfigurationUpdate', 'StateUpdate', 'Action', 'AlarmContributorStateUpdate', 'AlarmContributorAction'] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
    ScanBy: Literal['TimestampDescending', 'TimestampAscending'] | None = None
