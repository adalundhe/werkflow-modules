from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheBatchStopUpdateActionRequest(BaseModel):
    ServiceUpdateName: StrictStr
    ReplicationGroupIds: list[StrictStr] | None = None
    CacheClusterIds: list[StrictStr] | None = None
