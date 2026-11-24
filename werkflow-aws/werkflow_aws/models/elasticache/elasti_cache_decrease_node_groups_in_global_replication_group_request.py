from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElastiCacheDecreaseNodeGroupsInGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    NodeGroupCount: StrictInt
    ApplyImmediately: StrictBool
    GlobalNodeGroupsToRemove: list[StrictStr] | None = None
    GlobalNodeGroupsToRetain: list[StrictStr] | None = None
