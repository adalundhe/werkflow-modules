from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerGetScheduleGroupRequest(BaseModel):
    Name: StrictStr
