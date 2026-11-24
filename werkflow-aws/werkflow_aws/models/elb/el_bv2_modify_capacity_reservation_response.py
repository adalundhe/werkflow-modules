from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .el_bv2_minimum_load_balancer_capacity import ELBv2MinimumLoadBalancerCapacity
from .el_bv2_zonal_capacity_reservation_state import ELBv2ZonalCapacityReservationState


class ELBv2ModifyCapacityReservationResponse(BaseModel):
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DecreaseRequestsRemaining: StrictInt | None = None
    MinimumLoadBalancerCapacity: ELBv2MinimumLoadBalancerCapacity | None = None
    CapacityReservationState: list[ELBv2ZonalCapacityReservationState] | None = None
    ResponseMetadata: dict[str, Any] | None = None
