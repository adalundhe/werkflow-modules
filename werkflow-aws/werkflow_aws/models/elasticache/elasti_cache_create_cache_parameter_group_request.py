from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateCacheParameterGroupRequest(BaseModel):
    CacheParameterGroupName: StrictStr
    CacheParameterGroupFamily: StrictStr
    Description: StrictStr
    Tags: list[ElastiCacheTag] | None = None
