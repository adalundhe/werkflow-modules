from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StorageGatewayCacheAttributes(BaseModel):
    CacheStaleTimeoutInSeconds: StrictInt | None = None
