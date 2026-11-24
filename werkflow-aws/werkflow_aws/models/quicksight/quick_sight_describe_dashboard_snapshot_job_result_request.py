from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDashboardSnapshotJobResultRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    SnapshotJobId: StrictStr
