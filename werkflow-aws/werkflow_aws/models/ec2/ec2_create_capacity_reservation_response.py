from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_reservation import EC2CapacityReservation


class EC2CreateCapacityReservationResponse(BaseModel):
    CapacityReservation: EC2CapacityReservation | None = None
    ResponseMetadata: dict[str, Any] | None = None
