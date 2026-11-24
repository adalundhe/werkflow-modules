from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeleteSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
