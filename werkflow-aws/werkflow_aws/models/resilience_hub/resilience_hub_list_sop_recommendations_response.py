from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_sop_recommendation import ResilienceHubSopRecommendation


class ResilienceHubListSopRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    sopRecommendations: list[ResilienceHubSopRecommendation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
