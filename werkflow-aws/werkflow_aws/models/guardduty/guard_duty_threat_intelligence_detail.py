from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyThreatIntelligenceDetail(BaseModel):
    ThreatListName: StrictStr | None = None
    ThreatNames: list[StrictStr] | None = None
    ThreatFileSha256: StrictStr | None = None
