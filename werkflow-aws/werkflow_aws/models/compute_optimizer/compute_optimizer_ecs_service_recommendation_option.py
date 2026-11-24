from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .compute_optimizer_container_recommendation import ComputeOptimizerContainerRecommendation
from .compute_optimizer_ecs_savings_opportunity_after_discounts import ComputeOptimizerECSSavingsOpportunityAfterDiscounts
from .compute_optimizer_ecs_service_projected_utilization_metric import ComputeOptimizerECSServiceProjectedUtilizationMetric
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity


class ComputeOptimizerECSServiceRecommendationOption(BaseModel):
    memory: StrictInt | None = None
    cpu: StrictInt | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    savingsOpportunityAfterDiscounts: ComputeOptimizerECSSavingsOpportunityAfterDiscounts | None = None
    projectedUtilizationMetrics: list[ComputeOptimizerECSServiceProjectedUtilizationMetric] | None = None
    containerRecommendations: list[ComputeOptimizerContainerRecommendation] | None = None
