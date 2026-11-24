from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .scheduler_tag import SchedulerTag


class SchedulerCreateScheduleGroupRequest(BaseModel):
    Name: StrictStr
    Tags: list[SchedulerTag] | None = None
    ClientToken: StrictStr | None = None
