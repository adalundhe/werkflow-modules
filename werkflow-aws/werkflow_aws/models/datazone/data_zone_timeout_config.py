from __future__ import annotations
from pydantic import BaseModel, StrictInt


class DataZoneTimeoutConfig(BaseModel):
    runTimeoutInMinutes: StrictInt | None = None
