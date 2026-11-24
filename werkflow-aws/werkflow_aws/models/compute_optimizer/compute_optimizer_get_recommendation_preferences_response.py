from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_recommendation_preferences_detail import ComputeOptimizerRecommendationPreferencesDetail


class ComputeOptimizerGetRecommendationPreferencesResponse(BaseModel):
    nextToken: StrictStr | None = None
    recommendationPreferencesDetails: list[ComputeOptimizerRecommendationPreferencesDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
