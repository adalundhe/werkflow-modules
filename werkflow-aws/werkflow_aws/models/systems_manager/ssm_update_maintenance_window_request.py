from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMUpdateMaintenanceWindowRequest(BaseModel):
    WindowId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    StartDate: StrictStr | None = None
    EndDate: StrictStr | None = None
    Schedule: StrictStr | None = None
    ScheduleTimezone: StrictStr | None = None
    ScheduleOffset: StrictInt | None = None
    Duration: StrictInt | None = None
    Cutoff: StrictInt | None = None
    AllowUnassociatedTargets: StrictBool | None = None
    Enabled: StrictBool | None = None
    Replace: StrictBool | None = None
