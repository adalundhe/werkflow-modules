from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerDeleteScheduleRequest(BaseModel):
    Name: StrictStr
    GroupName: StrictStr | None = None
    ClientToken: StrictStr | None = None
