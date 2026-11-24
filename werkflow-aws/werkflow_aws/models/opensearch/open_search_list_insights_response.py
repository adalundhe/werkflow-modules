from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_insight import OpenSearchInsight


class OpenSearchListInsightsResponse(BaseModel):
    Insights: list[OpenSearchInsight] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
