from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ScheduledInstanceRecurrence(BaseModel):
    Frequency: StrictStr | None = None
    Interval: StrictInt | None = None
    OccurrenceDaySet: list[StrictInt] | None = None
    OccurrenceRelativeToEnd: StrictBool | None = None
    OccurrenceUnit: StrictStr | None = None
