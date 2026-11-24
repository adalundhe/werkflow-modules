from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStartDashboardRefreshRequest(BaseModel):
    DashboardId: StrictStr
    QueryParameterValues: dict[StrictStr, StrictStr] | None = None
