from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_serverless_cache_snapshot import ElastiCacheServerlessCacheSnapshot


class ElastiCacheCreateServerlessCacheSnapshotResponse(BaseModel):
    ServerlessCacheSnapshot: ElastiCacheServerlessCacheSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
