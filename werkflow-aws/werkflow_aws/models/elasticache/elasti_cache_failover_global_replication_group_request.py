from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheFailoverGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    PrimaryRegion: StrictStr
    PrimaryReplicationGroupId: StrictStr
