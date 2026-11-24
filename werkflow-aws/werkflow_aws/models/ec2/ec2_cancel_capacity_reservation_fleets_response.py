from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_reservation_fleet_cancellation_state import EC2CapacityReservationFleetCancellationState
from .ec2_failed_capacity_reservation_fleet_cancellation_result import EC2FailedCapacityReservationFleetCancellationResult


class EC2CancelCapacityReservationFleetsResponse(BaseModel):
    SuccessfulFleetCancellations: list[EC2CapacityReservationFleetCancellationState] | None = None
    FailedFleetCancellations: list[EC2FailedCapacityReservationFleetCancellationResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
