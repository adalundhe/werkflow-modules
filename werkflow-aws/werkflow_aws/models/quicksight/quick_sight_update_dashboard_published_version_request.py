from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateDashboardPublishedVersionRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    VersionNumber: StrictInt
