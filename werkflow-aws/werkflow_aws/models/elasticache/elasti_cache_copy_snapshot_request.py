from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCopySnapshotRequest(BaseModel):
    SourceSnapshotName: StrictStr
    TargetSnapshotName: StrictStr
    TargetBucket: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[ElastiCacheTag] | None = None
