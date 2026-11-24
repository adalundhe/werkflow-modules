from __future__ import annotations
from pydantic import BaseModel
from .ec2_fleet_spot_capacity_rebalance_request import EC2FleetSpotCapacityRebalanceRequest


class EC2FleetSpotMaintenanceStrategiesRequest(BaseModel):
    CapacityRebalance: EC2FleetSpotCapacityRebalanceRequest | None = None
