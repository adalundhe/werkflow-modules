from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_filter import ComputeOptimizerFilter
from .compute_optimizer_recommendation_preferences import ComputeOptimizerRecommendationPreferences


class ComputeOptimizerGetEC2InstanceRecommendationsRequest(BaseModel):
    instanceArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerFilter] | None = None
    accountIds: list[StrictStr] | None = None
    recommendationPreferences: ComputeOptimizerRecommendationPreferences | None = None
