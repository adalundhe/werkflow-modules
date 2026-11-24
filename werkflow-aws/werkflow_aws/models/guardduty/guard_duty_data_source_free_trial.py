from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyDataSourceFreeTrial(BaseModel):
    FreeTrialDaysRemaining: StrictInt | None = None
