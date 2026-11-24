from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_tag import SSMTag


class SSMCreateMaintenanceWindowRequest(BaseModel):
    Name: StrictStr
    Schedule: StrictStr
    Duration: StrictInt
    Cutoff: StrictInt
    AllowUnassociatedTargets: StrictBool
    Description: StrictStr | None = None
    StartDate: StrictStr | None = None
    EndDate: StrictStr | None = None
    ScheduleTimezone: StrictStr | None = None
    ScheduleOffset: StrictInt | None = None
    ClientToken: StrictStr | None = None
    Tags: list[SSMTag] | None = None
