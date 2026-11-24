from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_capacity_reservation_detail import SageMakerCapacityReservationDetail


class SageMakerDescribeCapacityReservationResponse(BaseModel):
    CapacityReservation: SageMakerCapacityReservationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
