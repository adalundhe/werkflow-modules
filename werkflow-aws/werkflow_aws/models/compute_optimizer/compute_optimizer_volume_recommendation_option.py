from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_ebs_savings_opportunity_after_discounts import ComputeOptimizerEBSSavingsOpportunityAfterDiscounts
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity
from .compute_optimizer_volume_configuration import ComputeOptimizerVolumeConfiguration


class ComputeOptimizerVolumeRecommendationOption(BaseModel):
    configuration: ComputeOptimizerVolumeConfiguration | None = None
    performanceRisk: StrictFloat | StrictInt | None = None
    rank: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerEBSSavingsOpportunityAfterDiscounts | None = None
