from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_space_quicksight_search_filter import QuickSightSpaceQuicksightSearchFilter


class QuickSightSearchSpacesRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightSpaceQuicksightSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
