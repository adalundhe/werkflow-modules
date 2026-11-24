from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheUnprocessedUpdateAction(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    ServiceUpdateName: StrictStr | None = None
    ErrorType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
