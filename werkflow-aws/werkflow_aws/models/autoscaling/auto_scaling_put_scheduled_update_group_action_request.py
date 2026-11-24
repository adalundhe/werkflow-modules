from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AutoScalingPutScheduledUpdateGroupActionRequest(BaseModel):
    AutoScalingGroupName: StrictStr
    ScheduledActionName: StrictStr
    Time: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Recurrence: StrictStr | None = None
    MinSize: StrictInt | None = None
    MaxSize: StrictInt | None = None
    DesiredCapacity: StrictInt | None = None
    TimeZone: StrictStr | None = None
