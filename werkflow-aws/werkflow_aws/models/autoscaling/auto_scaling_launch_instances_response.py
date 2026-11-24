from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_instance_collection import AutoScalingInstanceCollection
from .auto_scaling_launch_instances_error import AutoScalingLaunchInstancesError


class AutoScalingLaunchInstancesResponse(BaseModel):
    AutoScalingGroupName: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Instances: list[AutoScalingInstanceCollection] | None = None
    Errors: list[AutoScalingLaunchInstancesError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
