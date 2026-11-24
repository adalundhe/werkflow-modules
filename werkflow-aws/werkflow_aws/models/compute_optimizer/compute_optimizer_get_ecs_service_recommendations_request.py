from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_ecs_service_recommendation_filter import ComputeOptimizerECSServiceRecommendationFilter


class ComputeOptimizerGetECSServiceRecommendationsRequest(BaseModel):
    serviceArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerECSServiceRecommendationFilter] | None = None
    accountIds: list[StrictStr] | None = None
