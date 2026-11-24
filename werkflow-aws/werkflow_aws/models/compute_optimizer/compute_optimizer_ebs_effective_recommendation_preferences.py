from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_ebs_savings_estimation_mode import ComputeOptimizerEBSSavingsEstimationMode


class ComputeOptimizerEBSEffectiveRecommendationPreferences(BaseModel):
    savingsEstimationMode: ComputeOptimizerEBSSavingsEstimationMode | None = None
    lookBackPeriod: StrictStr | None = None
