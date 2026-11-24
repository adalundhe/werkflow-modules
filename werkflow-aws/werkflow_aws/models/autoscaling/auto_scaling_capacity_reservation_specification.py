from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .auto_scaling_capacity_reservation_target import AutoScalingCapacityReservationTarget


class AutoScalingCapacityReservationSpecification(BaseModel):
    CapacityReservationPreference: StrictStr | None = None
    CapacityReservationTarget: AutoScalingCapacityReservationTarget | None = None
