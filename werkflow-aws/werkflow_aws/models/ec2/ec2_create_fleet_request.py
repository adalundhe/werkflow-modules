from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_fleet_launch_template_config_request import EC2FleetLaunchTemplateConfigRequest
from .ec2_on_demand_options_request import EC2OnDemandOptionsRequest
from .ec2_reserved_capacity_options_request import EC2ReservedCapacityOptionsRequest
from .ec2_spot_options_request import EC2SpotOptionsRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_target_capacity_specification_request import EC2TargetCapacitySpecificationRequest


class EC2CreateFleetRequest(BaseModel):
    LaunchTemplateConfigs: list[EC2FleetLaunchTemplateConfigRequest]
    TargetCapacitySpecification: EC2TargetCapacitySpecificationRequest
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    SpotOptions: EC2SpotOptionsRequest | None = None
    OnDemandOptions: EC2OnDemandOptionsRequest | None = None
    ReservedCapacityOptions: EC2ReservedCapacityOptionsRequest | None = None
    ExcessCapacityTerminationPolicy: Literal['no-termination', 'termination'] | None = None
    TerminateInstancesWithExpiration: StrictBool | None = None
    Type: Literal['request', 'maintain', 'instant'] | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    ReplaceUnhealthyInstances: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    Context: StrictStr | None = None
