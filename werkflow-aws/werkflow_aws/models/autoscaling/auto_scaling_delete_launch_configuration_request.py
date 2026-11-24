from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingDeleteLaunchConfigurationRequest(BaseModel):
    LaunchConfigurationName: StrictStr
