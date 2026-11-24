from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_rdsdb_utilization_metric import ComputeOptimizerRDSDBUtilizationMetric
from .compute_optimizer_rds_instance_savings_opportunity_after_discounts import ComputeOptimizerRDSInstanceSavingsOpportunityAfterDiscounts
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity


class ComputeOptimizerRDSDBInstanceRecommendationOption(BaseModel):
    dbInstanceClass: StrictStr | None = None
    projectedUtilizationMetrics: list[ComputeOptimizerRDSDBUtilizationMetric] | None = None
    performanceRisk: StrictFloat | StrictInt | None = None
    rank: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerRDSInstanceSavingsOpportunityAfterDiscounts | None = None
