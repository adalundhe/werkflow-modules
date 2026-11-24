from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDeleteDBSnapshotRequest(BaseModel):
    DBSnapshotIdentifier: StrictStr
