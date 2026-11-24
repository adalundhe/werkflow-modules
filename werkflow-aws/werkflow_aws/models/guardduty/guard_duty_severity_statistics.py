from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutySeverityStatistics(BaseModel):
    LastGeneratedAt: datetime.datetime | StrictStr | None = None
    Severity: StrictFloat | StrictInt | None = None
    TotalFindings: StrictInt | None = None
