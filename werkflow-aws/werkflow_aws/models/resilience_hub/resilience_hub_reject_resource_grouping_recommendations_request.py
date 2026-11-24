from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_reject_grouping_recommendation_entry import ResilienceHubRejectGroupingRecommendationEntry


class ResilienceHubRejectResourceGroupingRecommendationsRequest(BaseModel):
    appArn: StrictStr
    entries: list[ResilienceHubRejectGroupingRecommendationEntry]
