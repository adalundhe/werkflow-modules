from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_cache_subnet_group import ElastiCacheCacheSubnetGroup


class ElastiCacheModifyCacheSubnetGroupResponse(BaseModel):
    CacheSubnetGroup: ElastiCacheCacheSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
