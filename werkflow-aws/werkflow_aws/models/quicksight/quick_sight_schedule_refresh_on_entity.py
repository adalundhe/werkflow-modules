from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightScheduleRefreshOnEntity(BaseModel):
    DayOfWeek: StrictStr | None = None
    DayOfMonth: StrictStr | None = None
