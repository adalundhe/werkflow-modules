from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyTimeWindowGroup(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    FindingCount: StrictInt | None = None
