from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_search_flows_filter import QuickSightSearchFlowsFilter


class QuickSightSearchFlowsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightSearchFlowsFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
