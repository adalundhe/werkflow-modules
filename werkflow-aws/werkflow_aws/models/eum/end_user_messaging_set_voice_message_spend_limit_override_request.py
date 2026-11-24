from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EndUserMessagingSetVoiceMessageSpendLimitOverrideRequest(BaseModel):
    MonthlyLimit: StrictInt
