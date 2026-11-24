from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDeleteApplicationSnapshotRequest(BaseModel):
    ApplicationName: StrictStr
    SnapshotName: StrictStr
    SnapshotCreationTimestamp: datetime.datetime | StrictStr
