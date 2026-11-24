from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_reserved_capacity_fallback_options import EC2ReservedCapacityFallbackOptions


class EC2ReservedCapacityOptions(BaseModel):
    AllocationStrategy: StrictStr | None = None
    ReservationTypes: list[StrictStr] | None = None
    ReservedCapacityFallbackOptions: EC2ReservedCapacityFallbackOptions | None = None
