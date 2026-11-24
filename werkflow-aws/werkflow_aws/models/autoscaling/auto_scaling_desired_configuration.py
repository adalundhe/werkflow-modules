from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification
from .auto_scaling_mixed_instances_policy import AutoScalingMixedInstancesPolicy


class AutoScalingDesiredConfiguration(BaseModel):
    LaunchTemplate: AutoScalingLaunchTemplateSpecification | None = None
    MixedInstancesPolicy: AutoScalingMixedInstancesPolicy | None = None
