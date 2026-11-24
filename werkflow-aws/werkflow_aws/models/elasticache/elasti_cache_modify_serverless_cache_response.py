from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_serverless_cache import ElastiCacheServerlessCache


class ElastiCacheModifyServerlessCacheResponse(BaseModel):
    ServerlessCache: ElastiCacheServerlessCache | None = None
    ResponseMetadata: dict[str, Any] | None = None
