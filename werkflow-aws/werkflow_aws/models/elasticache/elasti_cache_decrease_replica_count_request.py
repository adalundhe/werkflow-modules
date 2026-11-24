from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_configure_shard import ElastiCacheConfigureShard


class ElastiCacheDecreaseReplicaCountRequest(BaseModel):
    ReplicationGroupId: StrictStr
    ApplyImmediately: StrictBool
    NewReplicaCount: StrictInt | None = None
    ReplicaConfiguration: list[ElastiCacheConfigureShard] | None = None
    ReplicasToRemove: list[StrictStr] | None = None
