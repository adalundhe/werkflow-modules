from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ElastiCacheECPUPerSecond(BaseModel):
    Maximum: StrictInt | None = None
    Minimum: StrictInt | None = None
