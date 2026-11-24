from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_snapshot_configuration import QuickSightSnapshotConfiguration
from .quick_sight_snapshot_user_configuration import QuickSightSnapshotUserConfiguration


class QuickSightStartDashboardSnapshotJobRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    SnapshotJobId: StrictStr
    SnapshotConfiguration: QuickSightSnapshotConfiguration
    UserConfiguration: QuickSightSnapshotUserConfiguration | None = None
