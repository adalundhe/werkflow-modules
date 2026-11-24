from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteServerlessCacheRequest(BaseModel):
    ServerlessCacheName: StrictStr
    FinalSnapshotName: StrictStr | None = None
