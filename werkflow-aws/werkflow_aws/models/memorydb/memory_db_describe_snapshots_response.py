from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_snapshot import MemoryDBSnapshot


class MemoryDBDescribeSnapshotsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Snapshots: list[MemoryDBSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
