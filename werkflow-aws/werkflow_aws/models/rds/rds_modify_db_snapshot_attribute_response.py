from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_snapshot_attributes_result import RDSDBSnapshotAttributesResult


class RDSModifyDBSnapshotAttributeResponse(BaseModel):
    DBSnapshotAttributesResult: RDSDBSnapshotAttributesResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
