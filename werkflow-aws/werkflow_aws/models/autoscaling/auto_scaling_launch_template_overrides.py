from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .auto_scaling_instance_requirements import AutoScalingInstanceRequirements
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification


class AutoScalingLaunchTemplateOverrides(BaseModel):
    InstanceType: StrictStr | None = None
    WeightedCapacity: StrictStr | None = None
    LaunchTemplateSpecification: AutoScalingLaunchTemplateSpecification | None = None
    InstanceRequirements: AutoScalingInstanceRequirements | None = None
    ImageId: StrictStr | None = None
