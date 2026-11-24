from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .non_working_day import NonWorkingDay


class WorkingDaysConfig(BaseModel):
    friday: StrictBool | None = None
    id: StrictInt | None = None
    monday: StrictBool | None = None
    nonWorkingDays: list[NonWorkingDay] | None = None
    saturday: StrictBool | None = None
    sunday: StrictBool | None = None
    thursday: StrictBool | None = None
    timezoneId: StrictStr | None = None
    tuesday: StrictBool | None = None
    wednesday: StrictBool | None = None
