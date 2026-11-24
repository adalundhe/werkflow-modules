from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_fleet_capacity_reservation_target_request import EC2FleetCapacityReservationTargetRequest
from .ec2_reserved_capacity_fallback_options_request import EC2ReservedCapacityFallbackOptionsRequest


class EC2ReservedCapacityOptionsRequest(BaseModel):
    AllocationStrategy: Literal['prioritized'] | None = None
    ReservationTypes: list[Literal['on-demand-capacity-reservation', 'capacity-block', 'interruptible-capacity-reservation']] | None = None
    CapacityReservationTarget: EC2FleetCapacityReservationTargetRequest | None = None
    ReservedCapacityFallbackOptions: EC2ReservedCapacityFallbackOptionsRequest | None = None
