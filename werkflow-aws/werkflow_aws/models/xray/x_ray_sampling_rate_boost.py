from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class XRaySamplingRateBoost(BaseModel):
    MaxRate: StrictFloat | StrictInt | None = None
    CooldownWindowMinutes: StrictInt | None = None
