from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_cache_parameter_group import ElastiCacheCacheParameterGroup


class ElastiCacheCreateCacheParameterGroupResponse(BaseModel):
    CacheParameterGroup: ElastiCacheCacheParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
