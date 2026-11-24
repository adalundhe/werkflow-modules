from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupIdSuffix: StrictStr
    PrimaryReplicationGroupId: StrictStr
    GlobalReplicationGroupDescription: StrictStr | None = None
    Tags: list[ElastiCacheTag] | None = None
