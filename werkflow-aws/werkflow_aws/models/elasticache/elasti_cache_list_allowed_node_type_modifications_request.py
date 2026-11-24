from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheListAllowedNodeTypeModificationsRequest(BaseModel):
    CacheClusterId: StrictStr | None = None
    ReplicationGroupId: StrictStr | None = None
