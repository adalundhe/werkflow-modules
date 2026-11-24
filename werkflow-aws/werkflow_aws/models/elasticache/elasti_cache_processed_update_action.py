from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheProcessedUpdateAction(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    ServiceUpdateName: StrictStr | None = None
    UpdateActionStatus: StrictStr | None = None
