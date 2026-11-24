from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheTestFailoverRequest(BaseModel):
    ReplicationGroupId: StrictStr
    NodeGroupId: StrictStr
