from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LightsailDiskSnapshotInfo(BaseModel):
    sizeInGb: StrictInt | None = None
