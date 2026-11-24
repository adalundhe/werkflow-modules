from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_insight_entity import OpenSearchInsightEntity


class OpenSearchDescribeInsightDetailsRequest(BaseModel):
    Entity: OpenSearchInsightEntity
    InsightId: StrictStr
    ShowHtmlContent: StrictBool | None = None
