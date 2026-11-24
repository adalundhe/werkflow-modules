from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_capacity_reservation_options import EC2CapacityReservationOptions


class EC2OnDemandOptions(BaseModel):
    AllocationStrategy: StrictStr | None = None
    CapacityReservationOptions: EC2CapacityReservationOptions | None = None
    SingleInstanceType: StrictBool | None = None
    SingleAvailabilityZone: StrictBool | None = None
    MinTargetCapacity: StrictInt | None = None
    MaxTotalPrice: StrictStr | None = None
