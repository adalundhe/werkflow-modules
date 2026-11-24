from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCopyServerlessCacheSnapshotRequest(BaseModel):
    SourceServerlessCacheSnapshotName: StrictStr
    TargetServerlessCacheSnapshotName: StrictStr
    KmsKeyId: StrictStr | None = None
    Tags: list[ElastiCacheTag] | None = None
