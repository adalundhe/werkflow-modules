from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteCacheParameterGroupRequest(BaseModel):
    CacheParameterGroupName: StrictStr
