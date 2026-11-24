from __future__ import annotations
from pydantic import BaseModel
from .ec2_fleet_spot_capacity_rebalance import EC2FleetSpotCapacityRebalance


class EC2FleetSpotMaintenanceStrategies(BaseModel):
    CapacityRebalance: EC2FleetSpotCapacityRebalance | None = None
