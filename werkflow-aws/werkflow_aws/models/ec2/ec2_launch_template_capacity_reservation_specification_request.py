from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_capacity_reservation_target import EC2CapacityReservationTarget


class EC2LaunchTemplateCapacityReservationSpecificationRequest(BaseModel):
    CapacityReservationPreference: Literal['capacity-reservations-only', 'open', 'none'] | None = None
    CapacityReservationTarget: EC2CapacityReservationTarget | None = None
