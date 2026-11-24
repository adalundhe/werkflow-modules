from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_capacity_reservation import RDSDBCapacityReservation


class RDSDescribeDBCapacityReservationsResponse(BaseModel):
    DBCapacityReservations: list[RDSDBCapacityReservation] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
