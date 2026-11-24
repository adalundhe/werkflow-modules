from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDeleteThreatIntelSetRequest(BaseModel):
    DetectorId: StrictStr
    ThreatIntelSetId: StrictStr
