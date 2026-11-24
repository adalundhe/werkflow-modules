from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_data_source_search_filter import QuickSightDataSourceSearchFilter


class QuickSightSearchDataSourcesRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightDataSourceSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
