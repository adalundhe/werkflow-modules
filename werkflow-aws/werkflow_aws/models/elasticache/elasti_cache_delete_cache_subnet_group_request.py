from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteCacheSubnetGroupRequest(BaseModel):
    CacheSubnetGroupName: StrictStr
