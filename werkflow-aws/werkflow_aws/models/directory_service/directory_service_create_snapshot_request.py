from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceCreateSnapshotRequest(BaseModel):
    DirectoryId: StrictStr
    Name: StrictStr | None = None
