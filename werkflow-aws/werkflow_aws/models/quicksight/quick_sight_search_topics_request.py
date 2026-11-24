from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_search_filter import QuickSightTopicSearchFilter


class QuickSightSearchTopicsRequest(BaseModel):
    AwsAccountId: StrictStr
    Filters: list[QuickSightTopicSearchFilter]
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
