from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_engine_version import ElastiCacheCacheEngineVersion


class ElastiCacheDescribeCacheEngineVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    CacheEngineVersions: list[ElastiCacheCacheEngineVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
