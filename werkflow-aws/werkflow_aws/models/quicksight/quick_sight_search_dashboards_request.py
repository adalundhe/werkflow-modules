from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_dashboard_search_filter import QuickSightDashboardSearchFilter


class QuickSightSearchDashboardsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightDashboardSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
