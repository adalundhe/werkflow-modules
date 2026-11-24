from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Literal


class CloudWatchDescribeAlarmsRequest(BaseModel):
    AlarmNames: list[StrictStr] | None = None
    AlarmNamePrefix: StrictStr | None = None
    AlarmTypes: list[Literal['CompositeAlarm', 'MetricAlarm']] | None = None
    ChildrenOfAlarmName: StrictStr | None = None
    ParentsOfAlarmName: StrictStr | None = None
    StateValue: Literal['OK', 'ALARM', 'INSUFFICIENT_DATA'] | None = None
    ActionPrefix: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    NextToken: StrictStr | None = None
