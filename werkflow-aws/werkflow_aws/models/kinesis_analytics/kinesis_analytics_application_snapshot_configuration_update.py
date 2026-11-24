from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsApplicationSnapshotConfigurationUpdate(BaseModel):
    SnapshotsEnabledUpdate: StrictBool
    SnapshotModeUpdate: Literal['APPLICATION_SNAPSHOTS_LEGACY', 'ENHANCED_SNAPSHOTS'] | None = None
