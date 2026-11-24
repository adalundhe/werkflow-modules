from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyRepresentativeFinding(BaseModel):
    ResourceType: StrictStr | None = None
    Identifier: StrictStr | None = None
    FindingId: StrictStr | None = None
    FindingCount: StrictInt | None = None
    RiskLevel: StrictStr | None = None
    RiskRationale: StrictStr | None = None
