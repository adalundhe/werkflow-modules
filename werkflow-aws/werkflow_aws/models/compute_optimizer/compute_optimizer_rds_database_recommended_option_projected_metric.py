from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_rds_database_projected_metric import ComputeOptimizerRDSDatabaseProjectedMetric


class ComputeOptimizerRDSDatabaseRecommendedOptionProjectedMetric(BaseModel):
    recommendedDBInstanceClass: StrictStr | None = None
    rank: StrictInt | None = None
    projectedMetrics: list[ComputeOptimizerRDSDatabaseProjectedMetric] | None = None
