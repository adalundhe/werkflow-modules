from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_capacity_reservation_options_request import EC2CapacityReservationOptionsRequest


class EC2OnDemandOptionsRequest(BaseModel):
    AllocationStrategy: Literal['lowest-price', 'prioritized'] | None = None
    CapacityReservationOptions: EC2CapacityReservationOptionsRequest | None = None
    SingleInstanceType: StrictBool | None = None
    SingleAvailabilityZone: StrictBool | None = None
    MinTargetCapacity: StrictInt | None = None
    MaxTotalPrice: StrictStr | None = None
