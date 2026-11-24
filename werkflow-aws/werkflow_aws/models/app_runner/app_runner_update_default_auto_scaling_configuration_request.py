from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerUpdateDefaultAutoScalingConfigurationRequest(BaseModel):
    AutoScalingConfigurationArn: StrictStr
