from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_fleet import EC2CapacityReservationFleet


class EC2DescribeCapacityReservationFleetsResponse(BaseModel):
    CapacityReservationFleets: list[EC2CapacityReservationFleet] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
