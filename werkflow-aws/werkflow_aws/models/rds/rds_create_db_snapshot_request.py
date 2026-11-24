from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag import RDSTag


class RDSCreateDBSnapshotRequest(BaseModel):
    DBSnapshotIdentifier: StrictStr
    DBInstanceIdentifier: StrictStr
    Tags: list[RDSTag] | None = None
