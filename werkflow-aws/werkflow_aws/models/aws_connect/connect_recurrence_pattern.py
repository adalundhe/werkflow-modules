from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectRecurrencePattern(BaseModel):
    Frequency: StrictStr | None = None
    Interval: StrictInt | None = None
    ByMonth: list[StrictInt] | None = None
    ByMonthDay: list[StrictInt] | None = None
    ByWeekdayOccurrence: list[StrictInt] | None = None
