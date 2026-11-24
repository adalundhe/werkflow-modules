from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_snapshot import ElastiCacheSnapshot


class ElastiCacheCopySnapshotResponse(BaseModel):
    Snapshot: ElastiCacheSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
