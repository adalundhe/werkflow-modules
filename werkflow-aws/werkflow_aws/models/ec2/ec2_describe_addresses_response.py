from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_address import EC2Address


class EC2DescribeAddressesResponse(BaseModel):
    Addresses: list[EC2Address] | None = None
    ResponseMetadata: dict[str, Any] | None = None
