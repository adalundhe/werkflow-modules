from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElasticacheRebootCacheClusterRequest(BaseModel):
    CacheClusterId: StrictStr
    CacheNodeIdsToReboot: list[StrictStr]
