from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateSnapshotRequest(BaseModel):
    ClusterName: StrictStr
    SnapshotName: StrictStr
    KmsKeyId: StrictStr | None = None
    Tags: list[MemoryDBTag] | None = None
