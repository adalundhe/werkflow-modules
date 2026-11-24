from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_ecs_service_recommendation import ComputeOptimizerECSServiceRecommendation
from .compute_optimizer_get_recommendation_error import ComputeOptimizerGetRecommendationError


class ComputeOptimizerGetECSServiceRecommendationsResponse(BaseModel):
    nextToken: StrictStr | None = None
    ecsServiceRecommendations: list[ComputeOptimizerECSServiceRecommendation] | None = None
    errors: list[ComputeOptimizerGetRecommendationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
