from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyContinuousScanDetails(BaseModel):
    EndTime: datetime.datetime | StrictStr
    StartTime: datetime.datetime | StrictStr | None = None
