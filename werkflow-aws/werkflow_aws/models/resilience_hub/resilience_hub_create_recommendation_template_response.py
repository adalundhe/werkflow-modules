from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .resilience_hub_recommendation_template import ResilienceHubRecommendationTemplate


class ResilienceHubCreateRecommendationTemplateResponse(BaseModel):
    recommendationTemplate: ResilienceHubRecommendationTemplate | None = None
    ResponseMetadata: dict[str, Any] | None = None
