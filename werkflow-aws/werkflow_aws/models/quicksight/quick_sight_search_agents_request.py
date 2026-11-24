from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_agent_search_filter import QuickSightAgentSearchFilter


class QuickSightSearchAgentsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightAgentSearchFilter]
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
