from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCopySnapshotRequest(BaseModel):
    SourceSnapshotName: StrictStr
    TargetSnapshotName: StrictStr
    TargetBucket: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[MemoryDBTag] | None = None
