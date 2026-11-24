from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyAccountSummary(BaseModel):
    AccountId: StrictStr | None = None
    FindingCount: StrictInt | None = None
