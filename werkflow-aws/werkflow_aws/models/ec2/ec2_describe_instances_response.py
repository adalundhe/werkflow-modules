from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_reservation import EC2Reservation


class EC2DescribeInstancesResponse(BaseModel):
    Reservations: list[EC2Reservation] | None = None
    NextToken: StrictStr | None = None
