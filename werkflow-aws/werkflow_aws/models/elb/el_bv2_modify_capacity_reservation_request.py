from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .el_bv2_minimum_load_balancer_capacity import ELBv2MinimumLoadBalancerCapacity


class ELBv2ModifyCapacityReservationRequest(BaseModel):
    LoadBalancerArn: StrictStr
    MinimumLoadBalancerCapacity: ELBv2MinimumLoadBalancerCapacity | None = None
    ResetCapacityReservation: StrictBool | None = None
