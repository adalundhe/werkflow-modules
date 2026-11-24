from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_lambda_effective_recommendation_preferences import ComputeOptimizerLambdaEffectiveRecommendationPreferences
from .compute_optimizer_lambda_function_memory_recommendation_option import ComputeOptimizerLambdaFunctionMemoryRecommendationOption
from .compute_optimizer_lambda_function_utilization_metric import ComputeOptimizerLambdaFunctionUtilizationMetric
from .compute_optimizer_tag import ComputeOptimizerTag


class ComputeOptimizerLambdaFunctionRecommendation(BaseModel):
    functionArn: StrictStr | None = None
    functionVersion: StrictStr | None = None
    accountId: StrictStr | None = None
    currentMemorySize: StrictInt | None = None
    numberOfInvocations: StrictInt | None = None
    utilizationMetrics: list[ComputeOptimizerLambdaFunctionUtilizationMetric] | None = None
    lookbackPeriodInDays: StrictFloat | StrictInt | None = None
    lastRefreshTimestamp: datetime.datetime | StrictStr | None = None
    finding: StrictStr | None = None
    findingReasonCodes: list[StrictStr] | None = None
    memorySizeRecommendationOptions: list[ComputeOptimizerLambdaFunctionMemoryRecommendationOption] | None = None
    currentPerformanceRisk: StrictStr | None = None
    effectiveRecommendationPreferences: ComputeOptimizerLambdaEffectiveRecommendationPreferences | None = None
    tags: list[ComputeOptimizerTag] | None = None
