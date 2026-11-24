from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_global_replication_group import ElastiCacheGlobalReplicationGroup


class ElastiCacheDescribeGlobalReplicationGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    GlobalReplicationGroups: list[ElastiCacheGlobalReplicationGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
