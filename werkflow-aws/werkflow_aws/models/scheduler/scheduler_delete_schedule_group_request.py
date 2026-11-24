from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerDeleteScheduleGroupRequest(BaseModel):
    Name: StrictStr
    ClientToken: StrictStr | None = None
