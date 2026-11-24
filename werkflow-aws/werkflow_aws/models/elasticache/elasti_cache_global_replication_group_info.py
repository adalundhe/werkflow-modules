from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheGlobalReplicationGroupInfo(BaseModel):
    GlobalReplicationGroupId: StrictStr | None = None
    GlobalReplicationGroupMemberRole: StrictStr | None = None
