from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBDeleteSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
