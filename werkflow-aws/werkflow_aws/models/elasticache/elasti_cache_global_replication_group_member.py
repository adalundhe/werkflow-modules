from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheGlobalReplicationGroupMember(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    ReplicationGroupRegion: StrictStr | None = None
    Role: StrictStr | None = None
    AutomaticFailover: StrictStr | None = None
    Status: StrictStr | None = None
