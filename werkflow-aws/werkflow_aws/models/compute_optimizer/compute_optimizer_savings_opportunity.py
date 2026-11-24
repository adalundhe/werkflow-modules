from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_estimated_monthly_savings import ComputeOptimizerEstimatedMonthlySavings


class ComputeOptimizerSavingsOpportunity(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerEstimatedMonthlySavings | None = None
