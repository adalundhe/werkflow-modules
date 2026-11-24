from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_target_tracking_scaling_policy_configuration import SageMakerTargetTrackingScalingPolicyConfiguration


class SageMakerScalingPolicy(BaseModel):
    TargetTracking: SageMakerTargetTrackingScalingPolicyConfiguration | None = None
