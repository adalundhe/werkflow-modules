from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_ebs_effective_recommendation_preferences import ComputeOptimizerEBSEffectiveRecommendationPreferences
from .compute_optimizer_ebs_utilization_metric import ComputeOptimizerEBSUtilizationMetric
from .compute_optimizer_tag import ComputeOptimizerTag
from .compute_optimizer_volume_configuration import ComputeOptimizerVolumeConfiguration
from .compute_optimizer_volume_recommendation_option import ComputeOptimizerVolumeRecommendationOption


class ComputeOptimizerVolumeRecommendation(BaseModel):
    volumeArn: StrictStr | None = None
    accountId: StrictStr | None = None
    currentConfiguration: ComputeOptimizerVolumeConfiguration | None = None
    finding: StrictStr | None = None
    utilizationMetrics: list[ComputeOptimizerEBSUtilizationMetric] | None = None
    lookBackPeriodInDays: StrictFloat | StrictInt | None = None
    volumeRecommendationOptions: list[ComputeOptimizerVolumeRecommendationOption] | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    currentPerformanceRisk: StrictStr | None = None
    effectiveRecommendationPreferences: ComputeOptimizerEBSEffectiveRecommendationPreferences | None = None
    tags: list[ComputeOptimizerTag] | None = None
