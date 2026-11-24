from __future__ import annotations
from pydantic import BaseModel
from .ec2_fleet_launch_template_overrides import EC2FleetLaunchTemplateOverrides
from .ec2_fleet_launch_template_specification import EC2FleetLaunchTemplateSpecification


class EC2FleetLaunchTemplateConfig(BaseModel):
    LaunchTemplateSpecification: EC2FleetLaunchTemplateSpecification | None = None
    Overrides: list[EC2FleetLaunchTemplateOverrides] | None = None
