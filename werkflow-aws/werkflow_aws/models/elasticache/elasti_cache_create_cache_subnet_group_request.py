from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateCacheSubnetGroupRequest(BaseModel):
    CacheSubnetGroupName: StrictStr
    CacheSubnetGroupDescription: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[ElastiCacheTag] | None = None
