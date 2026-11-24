from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .ec2_launch_template_config import EC2LaunchTemplateConfig
from .ec2_load_balancers_config import EC2LoadBalancersConfig
from .ec2_spot_fleet_launch_specification import EC2SpotFleetLaunchSpecification
from .ec2_spot_maintenance_strategies import EC2SpotMaintenanceStrategies
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2SpotFleetRequestConfigData(BaseModel):
    AllocationStrategy: StrictStr | None = None
    OnDemandAllocationStrategy: StrictStr | None = None
    SpotMaintenanceStrategies: EC2SpotMaintenanceStrategies | None = None
    ClientToken: StrictStr | None = None
    ExcessCapacityTerminationPolicy: StrictStr | None = None
    FulfilledCapacity: StrictFloat | StrictInt | None = None
    OnDemandFulfilledCapacity: StrictFloat | StrictInt | None = None
    IamFleetRole: StrictStr | None = None
    LaunchSpecifications: list[EC2SpotFleetLaunchSpecification] | None = None
    LaunchTemplateConfigs: list[EC2LaunchTemplateConfig] | None = None
    SpotPrice: StrictStr | None = None
    TargetCapacity: StrictInt | None = None
    OnDemandTargetCapacity: StrictInt | None = None
    OnDemandMaxTotalPrice: StrictStr | None = None
    SpotMaxTotalPrice: StrictStr | None = None
    TerminateInstancesWithExpiration: StrictBool | None = None
    Type: StrictStr | None = None
    ValidFrom: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    ReplaceUnhealthyInstances: StrictBool | None = None
    InstanceInterruptionBehavior: StrictStr | None = None
    LoadBalancersConfig: EC2LoadBalancersConfig | None = None
    InstancePoolsToUseCount: StrictInt | None = None
    Context: StrictStr | None = None
    TargetCapacityUnitType: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
