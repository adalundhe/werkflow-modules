from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_rdsdb_recommendation_filter import ComputeOptimizerRDSDBRecommendationFilter
from .compute_optimizer_recommendation_preferences import ComputeOptimizerRecommendationPreferences


class ComputeOptimizerGetRDSDatabaseRecommendationsRequest(BaseModel):
    resourceArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerRDSDBRecommendationFilter] | None = None
    accountIds: list[StrictStr] | None = None
    recommendationPreferences: ComputeOptimizerRecommendationPreferences | None = None
