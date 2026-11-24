from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_set_search_filter import QuickSightDataSetSearchFilter


class QuickSightSearchDataSetsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightDataSetSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
