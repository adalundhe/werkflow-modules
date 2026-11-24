from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag import RDSTag


class RDSCreateDBClusterSnapshotRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
    DBClusterIdentifier: StrictStr
    Tags: list[RDSTag] | None = None
