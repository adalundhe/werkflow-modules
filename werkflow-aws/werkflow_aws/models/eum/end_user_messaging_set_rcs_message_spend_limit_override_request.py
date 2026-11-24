from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EndUserMessagingSetRcsMessageSpendLimitOverrideRequest(BaseModel):
    MonthlyLimit: StrictInt
