from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_parameter_group import ElastiCacheCacheParameterGroup


class ElastiCacheDescribeCacheParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    CacheParameterGroups: list[ElastiCacheCacheParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
