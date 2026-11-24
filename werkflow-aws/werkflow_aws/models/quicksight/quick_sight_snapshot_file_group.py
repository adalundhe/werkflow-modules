from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_file import QuickSightSnapshotFile


class QuickSightSnapshotFileGroup(BaseModel):
    Files: list[QuickSightSnapshotFile] | None = None
