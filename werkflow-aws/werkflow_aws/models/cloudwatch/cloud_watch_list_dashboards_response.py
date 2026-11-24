from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_dashboard_entry import CloudWatchDashboardEntry


class CloudWatchListDashboardsResponse(BaseModel):
    DashboardEntries: list[CloudWatchDashboardEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
