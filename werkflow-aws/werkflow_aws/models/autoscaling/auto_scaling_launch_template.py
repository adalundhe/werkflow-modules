from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_launch_template_overrides import AutoScalingLaunchTemplateOverrides
from .auto_scaling_launch_template_specification import AutoScalingLaunchTemplateSpecification


class AutoScalingLaunchTemplate(BaseModel):
    LaunchTemplateSpecification: AutoScalingLaunchTemplateSpecification | None = None
    Overrides: list[AutoScalingLaunchTemplateOverrides] | None = None
