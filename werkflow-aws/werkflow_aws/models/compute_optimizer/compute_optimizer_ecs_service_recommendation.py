from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_ecs_effective_recommendation_preferences import ComputeOptimizerECSEffectiveRecommendationPreferences
from .compute_optimizer_ecs_service_recommendation_option import ComputeOptimizerECSServiceRecommendationOption
from .compute_optimizer_ecs_service_utilization_metric import ComputeOptimizerECSServiceUtilizationMetric
from .compute_optimizer_service_configuration import ComputeOptimizerServiceConfiguration
from .compute_optimizer_tag import ComputeOptimizerTag


class ComputeOptimizerECSServiceRecommendation(BaseModel):
    serviceArn: StrictStr | None = None
    accountId: StrictStr | None = None
    currentServiceConfiguration: ComputeOptimizerServiceConfiguration | None = None
    utilizationMetrics: list[ComputeOptimizerECSServiceUtilizationMetric] | None = None
    lookbackPeriodInDays: StrictFloat | StrictInt | None = None
    launchType: StrictStr | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    finding: StrictStr | None = None
    findingReasonCodes: list[StrictStr] | None = None
    serviceRecommendationOptions: list[ComputeOptimizerECSServiceRecommendationOption] | None = None
    currentPerformanceRisk: StrictStr | None = None
    effectiveRecommendationPreferences: ComputeOptimizerECSEffectiveRecommendationPreferences | None = None
    tags: list[ComputeOptimizerTag] | None = None
