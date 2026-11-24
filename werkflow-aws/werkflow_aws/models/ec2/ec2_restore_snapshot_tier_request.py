from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2RestoreSnapshotTierRequest(BaseModel):
    SnapshotId: StrictStr
    TemporaryRestoreDays: StrictInt | None = None
    PermanentRestore: StrictBool | None = None
    DryRun: StrictBool | None = None
