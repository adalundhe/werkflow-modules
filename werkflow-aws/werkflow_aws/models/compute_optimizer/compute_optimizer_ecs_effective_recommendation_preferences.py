from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_ecs_savings_estimation_mode import ComputeOptimizerECSSavingsEstimationMode


class ComputeOptimizerECSEffectiveRecommendationPreferences(BaseModel):
    savingsEstimationMode: ComputeOptimizerECSSavingsEstimationMode | None = None
    lookBackPeriod: StrictStr | None = None
