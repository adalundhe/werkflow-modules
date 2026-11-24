from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyHighestSeverityThreatDetails(BaseModel):
    Severity: StrictStr | None = None
    ThreatName: StrictStr | None = None
    Count: StrictInt | None = None
