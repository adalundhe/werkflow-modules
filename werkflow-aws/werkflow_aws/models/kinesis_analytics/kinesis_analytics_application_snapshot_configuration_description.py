from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisAnalyticsApplicationSnapshotConfigurationDescription(BaseModel):
    SnapshotsEnabled: StrictBool | None = None
    SnapshotMode: StrictStr | None = None
