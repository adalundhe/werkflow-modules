from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_idle_savings_opportunity import ComputeOptimizerIdleSavingsOpportunity
from .compute_optimizer_idle_savings_opportunity_after_discounts import ComputeOptimizerIdleSavingsOpportunityAfterDiscounts
from .compute_optimizer_idle_utilization_metric import ComputeOptimizerIdleUtilizationMetric
from .compute_optimizer_tag import ComputeOptimizerTag


class ComputeOptimizerIdleRecommendation(BaseModel):
    resourceArn: StrictStr | None = None
    resourceId: StrictStr | None = None
    resourceType: StrictStr | None = None
    accountId: StrictStr | None = None
    finding: StrictStr | None = None
    findingDescription: StrictStr | None = None
    savingsOpportunity: ComputeOptimizerIdleSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerIdleSavingsOpportunityAfterDiscounts | None = None
    utilizationMetrics: list[ComputeOptimizerIdleUtilizationMetric] | None = None
    lookBackPeriodInDays: StrictFloat | StrictInt | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    tags: list[ComputeOptimizerTag] | None = None
