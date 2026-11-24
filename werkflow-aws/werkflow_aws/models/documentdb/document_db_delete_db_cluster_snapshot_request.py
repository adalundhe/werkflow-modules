from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteDBClusterSnapshotRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
