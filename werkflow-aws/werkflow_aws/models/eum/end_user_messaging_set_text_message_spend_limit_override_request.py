from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EndUserMessagingSetTextMessageSpendLimitOverrideRequest(BaseModel):
    MonthlyLimit: StrictInt
