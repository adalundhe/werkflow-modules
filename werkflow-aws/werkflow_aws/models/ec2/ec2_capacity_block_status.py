from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_capacity_reservation_status import EC2CapacityReservationStatus


class EC2CapacityBlockStatus(BaseModel):
    CapacityBlockId: StrictStr | None = None
    InterconnectStatus: StrictStr | None = None
    TotalCapacity: StrictInt | None = None
    TotalAvailableCapacity: StrictInt | None = None
    TotalUnavailableCapacity: StrictInt | None = None
    CapacityReservationStatuses: list[EC2CapacityReservationStatus] | None = None
