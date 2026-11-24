from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_fleet_spot_maintenance_strategies import EC2FleetSpotMaintenanceStrategies


class EC2SpotOptions(BaseModel):
    AllocationStrategy: StrictStr | None = None
    MaintenanceStrategies: EC2FleetSpotMaintenanceStrategies | None = None
    InstanceInterruptionBehavior: StrictStr | None = None
    InstancePoolsToUseCount: StrictInt | None = None
    SingleInstanceType: StrictBool | None = None
    SingleAvailabilityZone: StrictBool | None = None
    MinTargetCapacity: StrictInt | None = None
    MaxTotalPrice: StrictStr | None = None
