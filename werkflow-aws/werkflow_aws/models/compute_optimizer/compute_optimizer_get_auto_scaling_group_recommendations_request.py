from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_filter import ComputeOptimizerFilter
from .compute_optimizer_recommendation_preferences import ComputeOptimizerRecommendationPreferences


class ComputeOptimizerGetAutoScalingGroupRecommendationsRequest(BaseModel):
    accountIds: list[StrictStr] | None = None
    autoScalingGroupArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerFilter] | None = None
    recommendationPreferences: ComputeOptimizerRecommendationPreferences | None = None
