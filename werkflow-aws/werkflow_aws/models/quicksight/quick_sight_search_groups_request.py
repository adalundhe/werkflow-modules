from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_group_search_filter import QuickSightGroupSearchFilter


class QuickSightSearchGroupsRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    Filters: list[QuickSightGroupSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
