from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetThreatEntitySetRequest(BaseModel):
    DetectorId: StrictStr
    ThreatEntitySetId: StrictStr
