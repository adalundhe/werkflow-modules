from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_modification_quote import EC2CapacityReservationModificationQuote


class EC2DescribeCapacityReservationDateChangeQuotesResponse(BaseModel):
    CapacityReservationModificationQuotes: list[EC2CapacityReservationModificationQuote] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
