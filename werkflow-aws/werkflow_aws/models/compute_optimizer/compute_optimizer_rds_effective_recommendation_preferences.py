from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_rds_savings_estimation_mode import ComputeOptimizerRDSSavingsEstimationMode


class ComputeOptimizerRDSEffectiveRecommendationPreferences(BaseModel):
    cpuVendorArchitectures: list[StrictStr] | None = None
    enhancedInfrastructureMetrics: StrictStr | None = None
    lookBackPeriod: StrictStr | None = None
    savingsEstimationMode: ComputeOptimizerRDSSavingsEstimationMode | None = None
