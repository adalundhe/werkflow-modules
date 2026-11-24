from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_capacity_reservation import AthenaCapacityReservation


class AthenaListCapacityReservationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservations: list[AthenaCapacityReservation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
