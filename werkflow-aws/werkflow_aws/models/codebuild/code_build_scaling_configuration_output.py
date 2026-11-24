from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_target_tracking_scaling_configuration import CodeBuildTargetTrackingScalingConfiguration


class CodeBuildScalingConfigurationOutput(BaseModel):
    scalingType: StrictStr | None = None
    targetTrackingScalingConfigs: list[CodeBuildTargetTrackingScalingConfiguration] | None = None
    maxCapacity: StrictInt | None = None
    desiredCapacity: StrictInt | None = None
