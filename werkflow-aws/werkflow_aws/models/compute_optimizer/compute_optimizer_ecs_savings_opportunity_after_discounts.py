from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_ecs_estimated_monthly_savings import ComputeOptimizerECSEstimatedMonthlySavings


class ComputeOptimizerECSSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerECSEstimatedMonthlySavings | None = None
