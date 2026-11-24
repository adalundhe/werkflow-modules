from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsApplicationSnapshotConfiguration(BaseModel):
    SnapshotsEnabled: StrictBool
    SnapshotMode: Literal['APPLICATION_SNAPSHOTS_LEGACY', 'ENHANCED_SNAPSHOTS'] | None = None
