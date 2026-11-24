from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_snapshot_model import RDSDBSnapshotModel


class RDSModifyDBSnapshotResponse(BaseModel):
    DBSnapshot: RDSDBSnapshotModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
