from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .resilience_hub_accept_grouping_recommendation_entry import ResilienceHubAcceptGroupingRecommendationEntry


class ResilienceHubAcceptResourceGroupingRecommendationsRequest(BaseModel):
    appArn: StrictStr
    entries: list[ResilienceHubAcceptGroupingRecommendationEntry]
