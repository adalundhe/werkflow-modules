from __future__ import annotations
from pydantic import BaseModel
from .ec2_fleet_launch_template_specification import EC2FleetLaunchTemplateSpecification
from .ec2_launch_template_overrides import EC2LaunchTemplateOverrides


class EC2LaunchTemplateConfig(BaseModel):
    LaunchTemplateSpecification: EC2FleetLaunchTemplateSpecification | None = None
    Overrides: list[EC2LaunchTemplateOverrides] | None = None
