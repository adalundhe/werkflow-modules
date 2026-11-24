from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class EndUserMessagingDeleteMediaMessageSpendLimitOverrideResponse(BaseModel):
    MonthlyLimit: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
