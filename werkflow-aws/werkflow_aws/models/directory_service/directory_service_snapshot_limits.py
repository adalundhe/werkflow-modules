from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class DirectoryServiceSnapshotLimits(BaseModel):
    ManualSnapshotsLimit: StrictInt | None = None
    ManualSnapshotsCurrentCount: StrictInt | None = None
    ManualSnapshotsLimitReached: StrictBool | None = None
