from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_insight_selector import CloudTrailInsightSelector


class CloudTrailPutInsightSelectorsResponse(BaseModel):
    TrailARN: StrictStr | None = None
    InsightSelectors: list[CloudTrailInsightSelector] | None = None
    EventDataStoreArn: StrictStr | None = None
    InsightsDestination: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
