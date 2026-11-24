from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_search_apps_filter import QuickSightSearchAppsFilter


class QuickSightSearchAppsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightSearchAppsFilter]
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
