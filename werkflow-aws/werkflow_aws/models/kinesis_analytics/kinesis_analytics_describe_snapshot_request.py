from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDescribeSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
