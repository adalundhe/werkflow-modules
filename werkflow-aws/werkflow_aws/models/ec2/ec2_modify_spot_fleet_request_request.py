from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_launch_template_config import EC2LaunchTemplateConfig


class EC2ModifySpotFleetRequestRequest(BaseModel):
    SpotFleetRequestId: StrictStr
    LaunchTemplateConfigs: list[EC2LaunchTemplateConfig] | None = None
    OnDemandTargetCapacity: StrictInt | None = None
    Context: StrictStr | None = None
    TargetCapacity: StrictInt | None = None
    ExcessCapacityTerminationPolicy: Literal['noTermination', 'default'] | None = None
