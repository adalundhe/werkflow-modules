from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_billing_request import EC2CapacityReservationBillingRequest


class EC2DescribeCapacityReservationBillingRequestsResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservationBillingRequests: list[EC2CapacityReservationBillingRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
