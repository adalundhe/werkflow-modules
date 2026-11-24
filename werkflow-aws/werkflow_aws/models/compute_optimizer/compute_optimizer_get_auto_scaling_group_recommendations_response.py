from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_auto_scaling_group_recommendation import ComputeOptimizerAutoScalingGroupRecommendation
from .compute_optimizer_get_recommendation_error import ComputeOptimizerGetRecommendationError


class ComputeOptimizerGetAutoScalingGroupRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    autoScalingGroupRecommendations: list[ComputeOptimizerAutoScalingGroupRecommendation] | None = None
    errors: list[ComputeOptimizerGetRecommendationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
