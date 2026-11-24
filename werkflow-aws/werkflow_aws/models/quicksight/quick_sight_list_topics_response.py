from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_summary import QuickSightTopicSummary


class QuickSightListTopicsResponse(BaseModel):
    TopicsSummaries: list[QuickSightTopicSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
