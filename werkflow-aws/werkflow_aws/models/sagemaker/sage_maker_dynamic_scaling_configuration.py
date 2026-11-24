from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_scaling_policy import SageMakerScalingPolicy


class SageMakerDynamicScalingConfiguration(BaseModel):
    MinCapacity: StrictInt | None = None
    MaxCapacity: StrictInt | None = None
    ScaleInCooldown: StrictInt | None = None
    ScaleOutCooldown: StrictInt | None = None
    ScalingPolicies: list[SageMakerScalingPolicy] | None = None
