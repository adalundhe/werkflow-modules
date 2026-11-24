from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyGetThreatIntelSetRequest(BaseModel):
    DetectorId: StrictStr
    ThreatIntelSetId: StrictStr
