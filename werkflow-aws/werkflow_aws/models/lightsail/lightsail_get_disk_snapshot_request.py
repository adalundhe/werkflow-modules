from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDiskSnapshotRequest(BaseModel):
    diskSnapshotName: StrictStr
