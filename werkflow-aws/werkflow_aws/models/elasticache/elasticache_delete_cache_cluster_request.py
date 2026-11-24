from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElasticacheDeleteCacheClusterRequest(BaseModel):
    CacheClusterId: StrictStr
    FinalSnapshotIdentifier: StrictStr | None = None
