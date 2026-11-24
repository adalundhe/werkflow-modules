from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ElastiCacheCompleteMigrationRequest(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    ServerlessCacheName: StrictStr | None = None
    Force: StrictBool | None = None
