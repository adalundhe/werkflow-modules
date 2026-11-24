from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .memory_db_snapshot import MemoryDBSnapshot


class MemoryDBCopySnapshotResponse(BaseModel):
    Snapshot: MemoryDBSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
