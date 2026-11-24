from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_recommendation_template import ResilienceHubRecommendationTemplate


class ResilienceHubListRecommendationTemplatesResponse(BaseModel):
    nextToken: StrictStr | None = None
    recommendationTemplates: list[ResilienceHubRecommendationTemplate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
