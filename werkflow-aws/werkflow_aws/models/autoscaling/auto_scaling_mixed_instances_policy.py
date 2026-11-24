from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_instances_distribution import AutoScalingInstancesDistribution
from .auto_scaling_launch_template import AutoScalingLaunchTemplate


class AutoScalingMixedInstancesPolicy(BaseModel):
    LaunchTemplate: AutoScalingLaunchTemplate | None = None
    InstancesDistribution: AutoScalingInstancesDistribution | None = None
