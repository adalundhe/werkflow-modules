from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMGetMaintenanceWindowResponse(BaseModel):
    WindowId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    StartDate: StrictStr | None = None
    EndDate: StrictStr | None = None
    Schedule: StrictStr | None = None
    ScheduleTimezone: StrictStr | None = None
    ScheduleOffset: StrictInt | None = None
    NextExecutionTime: StrictStr | None = None
    Duration: StrictInt | None = None
    Cutoff: StrictInt | None = None
    AllowUnassociatedTargets: StrictBool | None = None
    Enabled: StrictBool | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    ModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
