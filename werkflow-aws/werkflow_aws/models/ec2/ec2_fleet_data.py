from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .ec2_describe_fleet_error import EC2DescribeFleetError
from .ec2_describe_fleets_instances import EC2DescribeFleetsInstances
from .ec2_fleet_launch_template_config import EC2FleetLaunchTemplateConfig
from .ec2_on_demand_options import EC2OnDemandOptions
from .ec2_reserved_capacity_options import EC2ReservedCapacityOptions
from .ec2_spot_options import EC2SpotOptions
from .ec2_tag_model import EC2TagModel
from .ec2_target_capacity_specification import EC2TargetCapacitySpecification


class EC2FleetData(BaseModel):
    ActivityStatus: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    FleetId: StrictStr | None = None
    FleetState: StrictStr | None = None
    ClientToken: StrictStr | None = None
    ExcessCapacityTerminationPolicy: StrictStr | None = None
    FulfilledCapacity: StrictFloat | StrictInt | None = None
    FulfilledOnDemandCapacity: StrictFloat | StrictInt | None = None
    LaunchTemplateConfigs: list[EC2FleetLaunchTemplateConfig] | None = None
    TargetCapacitySpecification: EC2TargetCapacitySpecification | None = None
    TerminateInstancesWithExpiration: StrictBool | None = None
    Type: StrictStr | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    ReplaceUnhealthyInstances: StrictBool | None = None
    SpotOptions: EC2SpotOptions | None = None
    OnDemandOptions: EC2OnDemandOptions | None = None
    ReservedCapacityOptions: EC2ReservedCapacityOptions | None = None
    Tags: list[EC2TagModel] | None = None
    Errors: list[EC2DescribeFleetError] | None = None
    Instances: list[EC2DescribeFleetsInstances] | None = None
    Context: StrictStr | None = None
