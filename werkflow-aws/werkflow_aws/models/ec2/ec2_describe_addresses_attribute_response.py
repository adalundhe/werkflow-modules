from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_address_attribute import EC2AddressAttribute


class EC2DescribeAddressesAttributeResponse(BaseModel):
    Addresses: list[EC2AddressAttribute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
