from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_auto_scaling_group_configuration import ComputeOptimizerAutoScalingGroupConfiguration
from .compute_optimizer_auto_scaling_group_recommendation_option import ComputeOptimizerAutoScalingGroupRecommendationOption
from .compute_optimizer_effective_recommendation_preferences import ComputeOptimizerEffectiveRecommendationPreferences
from .compute_optimizer_gpu_info import ComputeOptimizerGpuInfo
from .compute_optimizer_utilization_metric import ComputeOptimizerUtilizationMetric


class ComputeOptimizerAutoScalingGroupRecommendation(BaseModel):
    accountId: StrictStr | None = None
    autoScalingGroupArn: StrictStr | None = None
    autoScalingGroupName: StrictStr | None = None
    finding: StrictStr | None = None
    utilizationMetrics: list[ComputeOptimizerUtilizationMetric] | None = None
    lookBackPeriodInDays: StrictFloat | StrictInt | None = None
    currentConfiguration: ComputeOptimizerAutoScalingGroupConfiguration | None = None
    currentInstanceGpuInfo: ComputeOptimizerGpuInfo | None = None
    recommendationOptions: list[ComputeOptimizerAutoScalingGroupRecommendationOption] | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    currentPerformanceRisk: StrictStr | None = None
    effectiveRecommendationPreferences: ComputeOptimizerEffectiveRecommendationPreferences | None = None
    inferredWorkloadTypes: list[StrictStr] | None = None
