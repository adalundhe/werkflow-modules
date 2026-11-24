from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_serverless_cache import ElastiCacheServerlessCache


class ElastiCacheDescribeServerlessCachesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServerlessCaches: list[ElastiCacheServerlessCache] | None = None
    ResponseMetadata: dict[str, Any] | None = None
