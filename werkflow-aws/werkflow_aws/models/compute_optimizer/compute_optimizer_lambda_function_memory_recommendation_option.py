from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .compute_optimizer_lambda_function_memory_projected_metric import ComputeOptimizerLambdaFunctionMemoryProjectedMetric
from .compute_optimizer_lambda_savings_opportunity_after_discounts import ComputeOptimizerLambdaSavingsOpportunityAfterDiscounts
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity


class ComputeOptimizerLambdaFunctionMemoryRecommendationOption(BaseModel):
    rank: StrictInt | None = None
    memorySize: StrictInt | None = None
    projectedUtilizationMetrics: list[ComputeOptimizerLambdaFunctionMemoryProjectedMetric] | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerLambdaSavingsOpportunityAfterDiscounts | None = None
