from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMMaintenanceWindowIdentity(BaseModel):
    WindowId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Enabled: StrictBool | None = None
    Duration: StrictInt | None = None
    Cutoff: StrictInt | None = None
    Schedule: StrictStr | None = None
    ScheduleTimezone: StrictStr | None = None
    ScheduleOffset: StrictInt | None = None
    EndDate: StrictStr | None = None
    StartDate: StrictStr | None = None
    NextExecutionTime: StrictStr | None = None
