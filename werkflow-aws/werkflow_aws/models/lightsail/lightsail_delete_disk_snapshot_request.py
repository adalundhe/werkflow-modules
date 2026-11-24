from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteDiskSnapshotRequest(BaseModel):
    diskSnapshotName: StrictStr
