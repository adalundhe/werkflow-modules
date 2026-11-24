from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_scaling_policy_objective import SageMakerScalingPolicyObjective


class SageMakerGetScalingConfigurationRecommendationRequest(BaseModel):
    InferenceRecommendationsJobName: StrictStr
    RecommendationId: StrictStr | None = None
    EndpointName: StrictStr | None = None
    TargetCpuUtilizationPerCore: StrictInt | None = None
    ScalingPolicyObjective: SageMakerScalingPolicyObjective | None = None
