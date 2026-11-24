from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutyDateStatistics(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    LastGeneratedAt: datetime.datetime | StrictStr | None = None
    Severity: StrictFloat | StrictInt | None = None
    TotalFindings: StrictInt | None = None
