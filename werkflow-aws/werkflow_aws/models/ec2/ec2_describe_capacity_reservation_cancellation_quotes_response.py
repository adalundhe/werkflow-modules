from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_cancellation_quote import EC2CapacityReservationCancellationQuote


class EC2DescribeCapacityReservationCancellationQuotesResponse(BaseModel):
    CapacityReservationCancellationQuotes: list[EC2CapacityReservationCancellationQuote] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
