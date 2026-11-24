from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_grouping_recommendation import ResilienceHubGroupingRecommendation


class ResilienceHubListResourceGroupingRecommendationsResponse(BaseModel):
    groupingRecommendations: list[ResilienceHubGroupingRecommendation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
