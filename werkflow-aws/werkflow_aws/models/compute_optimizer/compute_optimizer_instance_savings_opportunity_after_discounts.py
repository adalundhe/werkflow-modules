from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_instance_estimated_monthly_savings import ComputeOptimizerInstanceEstimatedMonthlySavings


class ComputeOptimizerInstanceSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerInstanceEstimatedMonthlySavings | None = None
