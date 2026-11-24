from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_reservation_modification_quote import EC2CapacityReservationModificationQuote


class EC2CreateCapacityReservationDateChangeQuoteResponse(BaseModel):
    CapacityReservationModificationQuote: EC2CapacityReservationModificationQuote | None = None
    ResponseMetadata: dict[str, Any] | None = None
