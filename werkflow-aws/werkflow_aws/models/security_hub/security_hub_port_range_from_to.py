from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubPortRangeFromTo(BaseModel):
    From: StrictInt | None = None
    To: StrictInt | None = None
