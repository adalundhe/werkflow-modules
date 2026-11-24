from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDeleteDashboardsRequest(BaseModel):
    DashboardNames: list[StrictStr]
