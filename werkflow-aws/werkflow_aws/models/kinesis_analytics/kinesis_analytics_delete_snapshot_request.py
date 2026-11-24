from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDeleteSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
    SnapshotCreationTimestamp: datetime.datetime | StrictStr
