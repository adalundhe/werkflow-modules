from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyNetworkCounts(BaseModel):
    RequestCount: StrictInt | None = None
    TotalAttempts: StrictInt | None = None
    SuspiciousAttempts: StrictInt | None = None
    ResetAttempts: StrictInt | None = None
