from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMUpdateMaintenanceWindowResponse(BaseModel):
    WindowId: StrictStr | None = None
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
    ResponseMetadata: dict[str, Any] | None = None
