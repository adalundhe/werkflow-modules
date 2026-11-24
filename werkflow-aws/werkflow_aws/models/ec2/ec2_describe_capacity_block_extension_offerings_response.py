from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_block_extension_offering import EC2CapacityBlockExtensionOffering


class EC2DescribeCapacityBlockExtensionOfferingsResponse(BaseModel):
    CapacityBlockExtensionOfferings: list[EC2CapacityBlockExtensionOffering] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
