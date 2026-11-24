from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_capacity_reservation_cancellation_quote import EC2CapacityReservationCancellationQuote


class EC2CreateCapacityReservationCancellationQuoteResponse(BaseModel):
    CapacityReservationCancellationQuote: EC2CapacityReservationCancellationQuote | None = None
    ResponseMetadata: dict[str, Any] | None = None
