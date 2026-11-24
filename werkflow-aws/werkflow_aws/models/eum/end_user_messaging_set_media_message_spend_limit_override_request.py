from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EndUserMessagingSetMediaMessageSpendLimitOverrideRequest(BaseModel):
    MonthlyLimit: StrictInt
