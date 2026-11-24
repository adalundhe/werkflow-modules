from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_global_replication_group import ElastiCacheGlobalReplicationGroup


class ElastiCacheModifyGlobalReplicationGroupResponse(BaseModel):
    GlobalReplicationGroup: ElastiCacheGlobalReplicationGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
