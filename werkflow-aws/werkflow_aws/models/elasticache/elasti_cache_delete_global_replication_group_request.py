from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ElastiCacheDeleteGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    RetainPrimaryReplicationGroup: StrictBool
