from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_cancel_capacity_reservation_fleet_error import EC2CancelCapacityReservationFleetError


class EC2FailedCapacityReservationFleetCancellationResult(BaseModel):
    CapacityReservationFleetId: StrictStr | None = None
    CancelCapacityReservationFleetError: EC2CancelCapacityReservationFleetError | None = None
