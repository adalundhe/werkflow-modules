from __future__ import annotations
from pydantic import BaseModel
from .ec2_spot_capacity_rebalance import EC2SpotCapacityRebalance


class EC2SpotMaintenanceStrategies(BaseModel):
    CapacityRebalance: EC2SpotCapacityRebalance | None = None
