from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_info import EC2CapacityReservationInfo


class EC2CapacityReservationBillingRequest(BaseModel):
    CapacityReservationId: StrictStr | None = None
    RequestedBy: StrictStr | None = None
    UnusedReservationBillingOwnerId: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CapacityReservationInfo: EC2CapacityReservationInfo | None = None
