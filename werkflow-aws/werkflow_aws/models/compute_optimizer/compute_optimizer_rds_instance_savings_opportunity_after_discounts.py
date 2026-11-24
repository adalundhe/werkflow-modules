from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_rds_instance_estimated_monthly_savings import ComputeOptimizerRDSInstanceEstimatedMonthlySavings


class ComputeOptimizerRDSInstanceSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerRDSInstanceEstimatedMonthlySavings | None = None
