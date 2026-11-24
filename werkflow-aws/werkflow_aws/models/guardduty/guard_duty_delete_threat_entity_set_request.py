from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteThreatEntitySetRequest(BaseModel):
    DetectorId: StrictStr
    ThreatEntitySetId: StrictStr
