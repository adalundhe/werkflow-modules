from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasti_cache_regional_configuration import ElastiCacheRegionalConfiguration


class ElastiCacheIncreaseNodeGroupsInGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    NodeGroupCount: StrictInt
    ApplyImmediately: StrictBool
    RegionalConfigurations: list[ElastiCacheRegionalConfiguration] | None = None
