from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_snapshot_attribute import RDSDBSnapshotAttribute


class RDSDBSnapshotAttributesResult(BaseModel):
    DBSnapshotIdentifier: StrictStr | None = None
    DBSnapshotAttributes: list[RDSDBSnapshotAttribute] | None = None
