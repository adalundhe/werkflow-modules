from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_auto_scaling_group_estimated_monthly_savings import ComputeOptimizerAutoScalingGroupEstimatedMonthlySavings


class ComputeOptimizerAutoScalingGroupSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerAutoScalingGroupEstimatedMonthlySavings | None = None
