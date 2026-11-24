from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingMessagingLimits(BaseModel):
    RateLimits: dict[StrictStr, StrictInt] | None = None
    DailyMessageCaps: dict[StrictStr, StrictInt] | None = None
