from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyMemberAccountRanking(BaseModel):
    Rank: StrictInt | None = None
    AccountId: StrictStr | None = None
    FindingCount: StrictInt | None = None
    RiskLevel: StrictStr | None = None
    RiskRationale: StrictStr | None = None
