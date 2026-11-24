from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .compute_optimizer_lambda_estimated_monthly_savings import ComputeOptimizerLambdaEstimatedMonthlySavings


class ComputeOptimizerLambdaSavingsOpportunityAfterDiscounts(BaseModel):
    savingsOpportunityPercentage: StrictFloat | StrictInt | None = None
    estimatedMonthlySavings: ComputeOptimizerLambdaEstimatedMonthlySavings | None = None
