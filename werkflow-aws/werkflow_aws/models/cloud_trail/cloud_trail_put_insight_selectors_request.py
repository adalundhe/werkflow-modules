from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_insight_selector import CloudTrailInsightSelector


class CloudTrailPutInsightSelectorsRequest(BaseModel):
    InsightSelectors: list[CloudTrailInsightSelector]
    TrailName: StrictStr | None = None
    EventDataStore: StrictStr | None = None
    InsightsDestination: StrictStr | None = None
