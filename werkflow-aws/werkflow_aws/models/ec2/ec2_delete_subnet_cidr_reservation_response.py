from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_subnet_cidr_reservation import EC2SubnetCidrReservation


class EC2DeleteSubnetCidrReservationResponse(BaseModel):
    DeletedSubnetCidrReservation: EC2SubnetCidrReservation | None = None
    ResponseMetadata: dict[str, Any] | None = None
