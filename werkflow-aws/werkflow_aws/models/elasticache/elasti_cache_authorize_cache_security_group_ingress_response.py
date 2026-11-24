from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_cache_security_group import ElastiCacheCacheSecurityGroup


class ElastiCacheAuthorizeCacheSecurityGroupIngressResponse(BaseModel):
    CacheSecurityGroup: ElastiCacheCacheSecurityGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
