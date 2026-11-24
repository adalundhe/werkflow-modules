from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_security_group import ElastiCacheCacheSecurityGroup


class ElastiCacheDescribeCacheSecurityGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    CacheSecurityGroups: list[ElastiCacheCacheSecurityGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
