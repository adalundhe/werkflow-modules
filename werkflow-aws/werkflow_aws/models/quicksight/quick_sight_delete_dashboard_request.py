from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteDashboardRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    VersionNumber: StrictInt | None = None
