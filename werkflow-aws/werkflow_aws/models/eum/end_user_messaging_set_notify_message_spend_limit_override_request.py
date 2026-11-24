from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EndUserMessagingSetNotifyMessageSpendLimitOverrideRequest(BaseModel):
    MonthlyLimit: StrictInt
