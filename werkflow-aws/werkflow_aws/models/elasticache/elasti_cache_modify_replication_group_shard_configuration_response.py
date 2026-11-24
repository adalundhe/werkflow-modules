from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_replication_group import ElastiCacheReplicationGroup


class ElastiCacheModifyReplicationGroupShardConfigurationResponse(BaseModel):
    ReplicationGroup: ElastiCacheReplicationGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
