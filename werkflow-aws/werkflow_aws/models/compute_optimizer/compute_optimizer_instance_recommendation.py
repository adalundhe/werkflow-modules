from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_effective_recommendation_preferences import ComputeOptimizerEffectiveRecommendationPreferences
from .compute_optimizer_external_metric_status import ComputeOptimizerExternalMetricStatus
from .compute_optimizer_gpu_info import ComputeOptimizerGpuInfo
from .compute_optimizer_instance_recommendation_option import ComputeOptimizerInstanceRecommendationOption
from .compute_optimizer_recommendation_source import ComputeOptimizerRecommendationSource
from .compute_optimizer_tag import ComputeOptimizerTag
from .compute_optimizer_utilization_metric import ComputeOptimizerUtilizationMetric


class ComputeOptimizerInstanceRecommendation(BaseModel):
    instanceArn: StrictStr | None = None
    accountId: StrictStr | None = None
    instanceName: StrictStr | None = None
    currentInstanceType: StrictStr | None = None
    finding: StrictStr | None = None
    findingReasonCodes: list[StrictStr] | None = None
    utilizationMetrics: list[ComputeOptimizerUtilizationMetric] | None = None
    lookBackPeriodInDays: StrictFloat | StrictInt | None = None
    recommendationOptions: list[ComputeOptimizerInstanceRecommendationOption] | None = None
    recommendationSources: list[ComputeOptimizerRecommendationSource] | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    currentPerformanceRisk: StrictStr | None = None
    effectiveRecommendationPreferences: ComputeOptimizerEffectiveRecommendationPreferences | None = None
    inferredWorkloadTypes: list[StrictStr] | None = None
    instanceState: StrictStr | None = None
    tags: list[ComputeOptimizerTag] | None = None
    externalMetricStatus: ComputeOptimizerExternalMetricStatus | None = None
    currentInstanceGpuInfo: ComputeOptimizerGpuInfo | None = None
    idle: StrictStr | None = None
