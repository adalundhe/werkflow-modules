from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_host_reservation import EC2HostReservation


class EC2DescribeHostReservationsResponse(BaseModel):
    HostReservationSet: list[EC2HostReservation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
