from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_fleet_launch_template_config_request import EC2FleetLaunchTemplateConfigRequest
from .ec2_target_capacity_specification_request import EC2TargetCapacitySpecificationRequest


class EC2ModifyFleetRequest(BaseModel):
    FleetId: StrictStr
    DryRun: StrictBool | None = None
    ExcessCapacityTerminationPolicy: Literal['no-termination', 'termination'] | None = None
    LaunchTemplateConfigs: list[EC2FleetLaunchTemplateConfigRequest] | None = None
    TargetCapacitySpecification: EC2TargetCapacitySpecificationRequest | None = None
    Context: StrictStr | None = None
