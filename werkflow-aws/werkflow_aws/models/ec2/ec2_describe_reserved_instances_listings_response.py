from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_reserved_instances_listing import EC2ReservedInstancesListing


class EC2DescribeReservedInstancesListingsResponse(BaseModel):
    ReservedInstancesListings: list[EC2ReservedInstancesListing] | None = None
    ResponseMetadata: dict[str, Any] | None = None
