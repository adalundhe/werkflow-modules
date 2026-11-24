from __future__ import annotations
from pydantic import BaseModel
from .ec2_fleet_launch_template_overrides_request import EC2FleetLaunchTemplateOverridesRequest
from .ec2_fleet_launch_template_specification_request import EC2FleetLaunchTemplateSpecificationRequest


class EC2FleetLaunchTemplateConfigRequest(BaseModel):
    LaunchTemplateSpecification: EC2FleetLaunchTemplateSpecificationRequest | None = None
    Overrides: list[EC2FleetLaunchTemplateOverridesRequest] | None = None
