from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_projected_metric import ComputeOptimizerProjectedMetric


class ComputeOptimizerRecommendedOptionProjectedMetric(BaseModel):
    recommendedInstanceType: StrictStr | None = None
    rank: StrictInt | None = None
    projectedMetrics: list[ComputeOptimizerProjectedMetric] | None = None
