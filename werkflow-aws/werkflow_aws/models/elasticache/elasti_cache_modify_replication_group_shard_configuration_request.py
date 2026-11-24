from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_resharding_configuration import ElastiCacheReshardingConfiguration


class ElastiCacheModifyReplicationGroupShardConfigurationRequest(BaseModel):
    ReplicationGroupId: StrictStr
    NodeGroupCount: StrictInt
    ApplyImmediately: StrictBool
    ReshardingConfiguration: list[ElastiCacheReshardingConfiguration] | None = None
    NodeGroupsToRemove: list[StrictStr] | None = None
    NodeGroupsToRetain: list[StrictStr] | None = None
