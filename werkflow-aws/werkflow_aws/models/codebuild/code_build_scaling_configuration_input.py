from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .code_build_target_tracking_scaling_configuration import CodeBuildTargetTrackingScalingConfiguration


class CodeBuildScalingConfigurationInput(BaseModel):
    scalingType: Literal['TARGET_TRACKING_SCALING'] | None = None
    targetTrackingScalingConfigs: list[CodeBuildTargetTrackingScalingConfiguration] | None = None
    maxCapacity: StrictInt | None = None
