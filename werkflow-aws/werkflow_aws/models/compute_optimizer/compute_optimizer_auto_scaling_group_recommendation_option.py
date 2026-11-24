from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_auto_scaling_group_configuration import ComputeOptimizerAutoScalingGroupConfiguration
from .compute_optimizer_auto_scaling_group_savings_opportunity_after_discounts import ComputeOptimizerAutoScalingGroupSavingsOpportunityAfterDiscounts
from .compute_optimizer_gpu_info import ComputeOptimizerGpuInfo
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity
from .compute_optimizer_utilization_metric import ComputeOptimizerUtilizationMetric


class ComputeOptimizerAutoScalingGroupRecommendationOption(BaseModel):
    configuration: ComputeOptimizerAutoScalingGroupConfiguration | None = None
    instanceGpuInfo: ComputeOptimizerGpuInfo | None = None
    projectedUtilizationMetrics: list[ComputeOptimizerUtilizationMetric] | None = None
    performanceRisk: StrictFloat | StrictInt | None = None
    rank: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerAutoScalingGroupSavingsOpportunityAfterDiscounts | None = None
    migrationEffort: StrictStr | None = None
