from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBFailoverShardRequest(BaseModel):
    ClusterName: StrictStr
    ShardName: StrictStr
