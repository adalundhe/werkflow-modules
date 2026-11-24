from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDashboardPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
