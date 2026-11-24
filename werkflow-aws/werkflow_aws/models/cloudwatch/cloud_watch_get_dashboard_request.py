from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetDashboardRequest(BaseModel):
    DashboardName: StrictStr
