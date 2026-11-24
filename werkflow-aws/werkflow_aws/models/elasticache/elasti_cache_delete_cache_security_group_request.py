from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteCacheSecurityGroupRequest(BaseModel):
    CacheSecurityGroupName: StrictStr
