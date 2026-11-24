from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_subnet_group import ElastiCacheCacheSubnetGroup


class ElastiCacheDescribeCacheSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    CacheSubnetGroups: list[ElastiCacheCacheSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
