from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceGetSnapshotLimitsRequest(BaseModel):
    DirectoryId: StrictStr
