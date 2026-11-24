from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_recommendation_summary import ComputeOptimizerRecommendationSummary


class ComputeOptimizerGetRecommendationSummariesResponse(BaseModel):
    nextToken: StrictStr | None = None
    recommendationSummaries: list[ComputeOptimizerRecommendationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
