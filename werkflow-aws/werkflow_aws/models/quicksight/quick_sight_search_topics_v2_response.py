from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_topic_v2_summary import QuickSightTopicV2Summary


class QuickSightSearchTopicsV2Response(BaseModel):
    TopicSummaryList: list[QuickSightTopicV2Summary] | None = None
    NextToken: StrictStr | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
