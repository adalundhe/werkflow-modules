from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDashboardSnapshotJobRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    SnapshotJobId: StrictStr
