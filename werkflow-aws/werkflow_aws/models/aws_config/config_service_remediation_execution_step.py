from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceRemediationExecutionStep(BaseModel):
    Name: StrictStr | None = None
    State: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    StopTime: datetime.datetime | StrictStr | None = None
