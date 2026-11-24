from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasticache_tag import ElasticacheTag


class ElasticacheCreateSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
    ReplicationGroupId: StrictStr | None = None
    CacheClusterId: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[ElasticacheTag] | None = None
