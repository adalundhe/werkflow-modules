from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .compute_optimizer_recommended_option_projected_metric import ComputeOptimizerRecommendedOptionProjectedMetric


class ComputeOptimizerGetEC2RecommendationProjectedMetricsResponse(BaseModel):
    recommendedOptionProjectedMetrics: list[ComputeOptimizerRecommendedOptionProjectedMetric] | None = None
    ResponseMetadata: dict[str, Any] | None = None
