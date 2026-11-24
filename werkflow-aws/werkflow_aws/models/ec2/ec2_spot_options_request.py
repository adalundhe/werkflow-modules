from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_fleet_spot_maintenance_strategies_request import EC2FleetSpotMaintenanceStrategiesRequest


class EC2SpotOptionsRequest(BaseModel):
    AllocationStrategy: Literal['lowest-price', 'diversified', 'capacity-optimized', 'capacity-optimized-prioritized', 'price-capacity-optimized'] | None = None
    MaintenanceStrategies: EC2FleetSpotMaintenanceStrategiesRequest | None = None
    InstanceInterruptionBehavior: Literal['hibernate', 'stop', 'terminate'] | None = None
    InstancePoolsToUseCount: StrictInt | None = None
    SingleInstanceType: StrictBool | None = None
    SingleAvailabilityZone: StrictBool | None = None
    MinTargetCapacity: StrictInt | None = None
    MaxTotalPrice: StrictStr | None = None
