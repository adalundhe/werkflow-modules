from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_launch_configuration import AutoScalingLaunchConfiguration


class AutoScalingDescribeLaunchConfigurationsResponse(BaseModel):
    LaunchConfigurations: list[AutoScalingLaunchConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
