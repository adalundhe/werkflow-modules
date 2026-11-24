from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_time_window_group import GuardDutyTimeWindowGroup


class GuardDutyTrend(BaseModel):
    Granularity: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    TotalFindings: StrictInt | None = None
    ByTimeWindow: list[GuardDutyTimeWindowGroup] | None = None
