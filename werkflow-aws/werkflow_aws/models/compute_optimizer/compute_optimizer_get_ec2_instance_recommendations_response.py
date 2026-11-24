from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_get_recommendation_error import ComputeOptimizerGetRecommendationError
from .compute_optimizer_instance_recommendation import ComputeOptimizerInstanceRecommendation


class ComputeOptimizerGetEC2InstanceRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    instanceRecommendations: list[ComputeOptimizerInstanceRecommendation] | None = None
    errors: list[ComputeOptimizerGetRecommendationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
