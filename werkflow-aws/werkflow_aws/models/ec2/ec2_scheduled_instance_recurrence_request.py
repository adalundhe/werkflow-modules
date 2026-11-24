from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ScheduledInstanceRecurrenceRequest(BaseModel):
    Frequency: StrictStr | None = None
    Interval: StrictInt | None = None
    OccurrenceDays: list[StrictInt] | None = None
    OccurrenceRelativeToEnd: StrictBool | None = None
    OccurrenceUnit: StrictStr | None = None
