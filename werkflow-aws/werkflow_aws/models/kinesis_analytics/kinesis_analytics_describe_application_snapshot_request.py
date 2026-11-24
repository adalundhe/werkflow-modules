from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDescribeApplicationSnapshotRequest(BaseModel):
    ApplicationName: StrictStr
    SnapshotName: StrictStr
