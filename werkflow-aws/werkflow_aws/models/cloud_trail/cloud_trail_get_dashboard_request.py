from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetDashboardRequest(BaseModel):
    DashboardId: StrictStr
