from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation import EC2CapacityReservation


class EC2DescribeCapacityReservationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservations: list[EC2CapacityReservation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
