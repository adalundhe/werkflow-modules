from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TimeTrackingConfiguration(BaseModel):
    defaultUnit: StrictStr | None = None
    timeFormat: StrictStr | None = None
    workingDaysPerWeek: StrictFloat | StrictInt | None = None
    workingHoursPerDay: StrictFloat | StrictInt | None = None
