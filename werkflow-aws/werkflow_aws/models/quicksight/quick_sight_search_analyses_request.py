from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_analysis_search_filter import QuickSightAnalysisSearchFilter


class QuickSightSearchAnalysesRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightAnalysisSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
