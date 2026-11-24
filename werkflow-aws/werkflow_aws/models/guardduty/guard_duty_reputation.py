from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyReputation(BaseModel):
    FindingTimeDisposition: StrictStr | None = None
    CurrentDisposition: StrictStr | None = None
    ReputationComparison: StrictStr | None = None
