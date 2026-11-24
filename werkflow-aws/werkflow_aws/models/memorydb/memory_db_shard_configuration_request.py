from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MemoryDBShardConfigurationRequest(BaseModel):
    ShardCount: StrictInt | None = None
