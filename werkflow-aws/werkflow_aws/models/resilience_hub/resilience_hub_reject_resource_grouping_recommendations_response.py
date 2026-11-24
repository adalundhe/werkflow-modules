from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_failed_grouping_recommendation_entry import ResilienceHubFailedGroupingRecommendationEntry


class ResilienceHubRejectResourceGroupingRecommendationsResponse(BaseModel):
    appArn: StrictStr | None = None
    failedEntries: list[ResilienceHubFailedGroupingRecommendationEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
