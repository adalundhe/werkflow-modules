from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_ebs_estimated_monthly_savings import ComputeOptimizerEBSEstimatedMonthlySavings


class ComputeOptimizerEBSSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerEBSEstimatedMonthlySavings | None = None
