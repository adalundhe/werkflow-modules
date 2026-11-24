from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_component_recommendation import ResilienceHubComponentRecommendation


class ResilienceHubListAppComponentRecommendationsResponse(BaseModel):
    componentRecommendations: list[ResilienceHubComponentRecommendation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
