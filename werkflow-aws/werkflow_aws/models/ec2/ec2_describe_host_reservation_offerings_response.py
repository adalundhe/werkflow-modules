from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_host_offering import EC2HostOffering


class EC2DescribeHostReservationOfferingsResponse(BaseModel):
    NextToken: StrictStr | None = None
    OfferingSet: list[EC2HostOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
