from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_target_tracking_scaling_policy import LambdaTargetTrackingScalingPolicy


class LambdaCapacityProviderScalingConfig(BaseModel):
    MaxVCpuCount: StrictInt | None = None
    ScalingMode: StrictStr | None = None
    ScalingPolicies: list[LambdaTargetTrackingScalingPolicy] | None = None
