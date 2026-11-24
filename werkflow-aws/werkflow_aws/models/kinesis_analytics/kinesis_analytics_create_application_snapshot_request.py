from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsCreateApplicationSnapshotRequest(BaseModel):
    ApplicationName: StrictStr
    SnapshotName: StrictStr
