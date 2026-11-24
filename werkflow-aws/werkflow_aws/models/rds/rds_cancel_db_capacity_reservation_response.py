from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_capacity_reservation import RDSDBCapacityReservation


class RDSCancelDBCapacityReservationResponse(BaseModel):
    DBCapacityReservation: RDSDBCapacityReservation | None = None
    ResponseMetadata: dict[str, Any] | None = None
