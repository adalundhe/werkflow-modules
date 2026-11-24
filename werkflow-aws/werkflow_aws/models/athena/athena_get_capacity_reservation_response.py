from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_capacity_reservation import AthenaCapacityReservation


class AthenaGetCapacityReservationResponse(BaseModel):
    CapacityReservation: AthenaCapacityReservation | None = None
    ResponseMetadata: dict[str, Any] | None = None
