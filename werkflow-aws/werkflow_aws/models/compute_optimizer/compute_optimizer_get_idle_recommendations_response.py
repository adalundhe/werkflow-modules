from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_idle_recommendation import ComputeOptimizerIdleRecommendation
from .compute_optimizer_idle_recommendation_error import ComputeOptimizerIdleRecommendationError


class ComputeOptimizerGetIdleRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    idleRecommendations: list[ComputeOptimizerIdleRecommendation] | None = None
    errors: list[ComputeOptimizerIdleRecommendationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
