from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBClusterSnapshotRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
