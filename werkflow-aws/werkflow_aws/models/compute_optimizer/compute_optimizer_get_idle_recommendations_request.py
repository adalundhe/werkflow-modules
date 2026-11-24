from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_idle_recommendation_filter import ComputeOptimizerIdleRecommendationFilter
from .compute_optimizer_order_by import ComputeOptimizerOrderBy


class ComputeOptimizerGetIdleRecommendationsRequest(BaseModel):
    resourceArns: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[ComputeOptimizerIdleRecommendationFilter] | None = None
    accountIds: list[StrictStr] | None = None
    orderBy: ComputeOptimizerOrderBy | None = None
