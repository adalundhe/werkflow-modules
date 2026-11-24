from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_gpu_info import ComputeOptimizerGpuInfo
from .compute_optimizer_instance_savings_opportunity_after_discounts import ComputeOptimizerInstanceSavingsOpportunityAfterDiscounts
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity
from .compute_optimizer_utilization_metric import ComputeOptimizerUtilizationMetric


class ComputeOptimizerInstanceRecommendationOption(BaseModel):
    instanceType: StrictStr | None = None
    instanceGpuInfo: ComputeOptimizerGpuInfo | None = None
    projectedUtilizationMetrics: list[ComputeOptimizerUtilizationMetric] | None = None
    platformDifferences: list[StrictStr] | None = None
    performanceRisk: StrictFloat | StrictInt | None = None
    rank: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerInstanceSavingsOpportunityAfterDiscounts | None = None
    migrationEffort: StrictStr | None = None
