from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_block_offering import EC2CapacityBlockOffering


class EC2DescribeCapacityBlockOfferingsResponse(BaseModel):
    CapacityBlockOfferings: list[EC2CapacityBlockOffering] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
