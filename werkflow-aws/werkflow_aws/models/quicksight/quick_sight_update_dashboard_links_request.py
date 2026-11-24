from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateDashboardLinksRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    LinkEntities: list[StrictStr]
