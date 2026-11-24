from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectUpdateContactScheduleRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ScheduledTime: datetime.datetime | StrictStr
