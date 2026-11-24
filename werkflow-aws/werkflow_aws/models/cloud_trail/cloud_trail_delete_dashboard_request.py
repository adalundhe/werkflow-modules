from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDeleteDashboardRequest(BaseModel):
    DashboardId: StrictStr
