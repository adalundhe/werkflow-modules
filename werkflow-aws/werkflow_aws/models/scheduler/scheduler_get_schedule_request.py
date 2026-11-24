from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerGetScheduleRequest(BaseModel):
    Name: StrictStr
    GroupName: StrictStr | None = None
