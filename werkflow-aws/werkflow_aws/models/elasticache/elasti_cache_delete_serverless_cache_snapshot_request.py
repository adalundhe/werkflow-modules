from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheDeleteServerlessCacheSnapshotRequest(BaseModel):
    ServerlessCacheSnapshotName: StrictStr
