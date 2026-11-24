from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDescribeAutoScalingConfigurationRequest(BaseModel):
    AutoScalingConfigurationArn: StrictStr
