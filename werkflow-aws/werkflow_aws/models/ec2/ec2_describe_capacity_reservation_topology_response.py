from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_reservation_topology import EC2CapacityReservationTopology


class EC2DescribeCapacityReservationTopologyResponse(BaseModel):
    NextToken: StrictStr | None = None
    CapacityReservations: list[EC2CapacityReservationTopology] | None = None
    ResponseMetadata: dict[str, Any] | None = None
