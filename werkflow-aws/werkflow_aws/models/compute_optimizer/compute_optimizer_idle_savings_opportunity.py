from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_idle_estimated_monthly_savings import ComputeOptimizerIdleEstimatedMonthlySavings


class ComputeOptimizerIdleSavingsOpportunity(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerIdleEstimatedMonthlySavings | None = None
