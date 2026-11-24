from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .compute_optimizer_ecs_service_recommended_option_projected_metric import ComputeOptimizerECSServiceRecommendedOptionProjectedMetric


class ComputeOptimizerGetECSServiceRecommendationProjectedMetricsResponse(BaseModel):
    recommendedOptionProjectedMetrics: list[ComputeOptimizerECSServiceRecommendedOptionProjectedMetric] | None = None
    ResponseMetadata: dict[str, Any] | None = None
