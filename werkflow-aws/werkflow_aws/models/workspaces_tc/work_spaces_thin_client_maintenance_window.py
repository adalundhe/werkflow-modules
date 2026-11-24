from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesThinClientMaintenanceWindow(BaseModel):
    type: StrictStr | None = None
    startTimeHour: StrictInt | None = None
    startTimeMinute: StrictInt | None = None
    endTimeHour: StrictInt | None = None
    endTimeMinute: StrictInt | None = None
    daysOfTheWeek: list[StrictStr] | None = None
    applyTimeOf: StrictStr | None = None
