from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_dynamic_scaling_configuration import SageMakerDynamicScalingConfiguration
from .sage_maker_scaling_policy_metric import SageMakerScalingPolicyMetric
from .sage_maker_scaling_policy_objective import SageMakerScalingPolicyObjective


class SageMakerGetScalingConfigurationRecommendationResponse(BaseModel):
    InferenceRecommendationsJobName: StrictStr | None = None
    RecommendationId: StrictStr | None = None
    EndpointName: StrictStr | None = None
    TargetCpuUtilizationPerCore: StrictInt | None = None
    ScalingPolicyObjective: SageMakerScalingPolicyObjective | None = None
    Metric: SageMakerScalingPolicyMetric | None = None
    DynamicScalingConfiguration: SageMakerDynamicScalingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
