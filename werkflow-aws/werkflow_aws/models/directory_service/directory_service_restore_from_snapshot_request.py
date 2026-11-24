from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRestoreFromSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
