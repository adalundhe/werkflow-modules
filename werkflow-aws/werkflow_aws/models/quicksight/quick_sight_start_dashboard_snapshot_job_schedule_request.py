from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStartDashboardSnapshotJobScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    ScheduleId: StrictStr
