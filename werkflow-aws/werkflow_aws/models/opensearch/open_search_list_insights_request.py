from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_insight_entity import OpenSearchInsightEntity
from .open_search_insight_time_range import OpenSearchInsightTimeRange


class OpenSearchListInsightsRequest(BaseModel):
    Entity: OpenSearchInsightEntity
    TimeRange: OpenSearchInsightTimeRange | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
