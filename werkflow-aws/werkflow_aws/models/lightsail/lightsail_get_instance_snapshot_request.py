from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetInstanceSnapshotRequest(BaseModel):
    instanceSnapshotName: StrictStr
