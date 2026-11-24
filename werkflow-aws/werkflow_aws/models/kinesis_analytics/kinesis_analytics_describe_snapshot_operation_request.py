from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDescribeSnapshotOperationRequest(BaseModel):
    SnapshotName: StrictStr
    SnapshotOperationId: StrictStr
