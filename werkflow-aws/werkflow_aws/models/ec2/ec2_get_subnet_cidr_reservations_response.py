from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_subnet_cidr_reservation import EC2SubnetCidrReservation


class EC2GetSubnetCidrReservationsResponse(BaseModel):
    SubnetIpv4CidrReservations: list[EC2SubnetCidrReservation] | None = None
    SubnetIpv6CidrReservations: list[EC2SubnetCidrReservation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
