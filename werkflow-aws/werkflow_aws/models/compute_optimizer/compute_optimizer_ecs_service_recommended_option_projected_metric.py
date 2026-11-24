from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .compute_optimizer_ecs_service_projected_metric import ComputeOptimizerECSServiceProjectedMetric


class ComputeOptimizerECSServiceRecommendedOptionProjectedMetric(BaseModel):
    recommendedCpuUnits: StrictInt | None = None
    recommendedMemorySize: StrictInt | None = None
    projectedMetrics: list[ComputeOptimizerECSServiceProjectedMetric] | None = None
