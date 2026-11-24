from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQWeeklyStartTime(BaseModel):
    DayOfWeek: StrictStr | None = None
    TimeOfDay: StrictStr | None = None
    TimeZone: StrictStr | None = None
