from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_type_offering import EC2InstanceTypeOffering


class EC2DescribeInstanceTypeOfferingsResponse(BaseModel):
    InstanceTypeOfferings: list[EC2InstanceTypeOffering] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
