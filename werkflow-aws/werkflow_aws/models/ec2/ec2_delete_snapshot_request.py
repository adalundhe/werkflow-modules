from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
    DryRun: StrictBool | None = None
