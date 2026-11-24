from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_dashboard_detail import CloudTrailDashboardDetail


class CloudTrailListDashboardsResponse(BaseModel):
    Dashboards: list[CloudTrailDashboardDetail] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
