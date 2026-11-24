from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .compute_optimizer_rds_database_recommended_option_projected_metric import ComputeOptimizerRDSDatabaseRecommendedOptionProjectedMetric


class ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsResponse(BaseModel):
    recommendedOptionProjectedMetrics: list[ComputeOptimizerRDSDatabaseRecommendedOptionProjectedMetric] | None = None
    ResponseMetadata: dict[str, Any] | None = None
