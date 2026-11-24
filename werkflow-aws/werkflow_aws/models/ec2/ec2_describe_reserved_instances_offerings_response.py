from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_reserved_instances_offering import EC2ReservedInstancesOffering


class EC2DescribeReservedInstancesOfferingsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedInstancesOfferings: list[EC2ReservedInstancesOffering] | None = None
    ResponseMetadata: dict[str, Any] | None = None
