from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDisassociateGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    ReplicationGroupId: StrictStr
    ReplicationGroupRegion: StrictStr
