from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_current_performance_risk_ratings import ComputeOptimizerCurrentPerformanceRiskRatings
from .compute_optimizer_idle_summary import ComputeOptimizerIdleSummary
from .compute_optimizer_inferred_workload_saving import ComputeOptimizerInferredWorkloadSaving
from .compute_optimizer_savings_opportunity import ComputeOptimizerSavingsOpportunity
from .compute_optimizer_summary import ComputeOptimizerSummary


class ComputeOptimizerRecommendationSummary(BaseModel):
    summaries: list[ComputeOptimizerSummary] | None = None
    idleSummaries: list[ComputeOptimizerIdleSummary] | None = None
    recommendationResourceType: StrictStr | None = None
    accountId: StrictStr | None = None
    savingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    idleSavingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    aggregatedSavingsOpportunity: ComputeOptimizerSavingsOpportunity | None = None
    currentPerformanceRiskRatings: ComputeOptimizerCurrentPerformanceRiskRatings | None = None
    inferredWorkloadSavings: list[ComputeOptimizerInferredWorkloadSaving] | None = None
