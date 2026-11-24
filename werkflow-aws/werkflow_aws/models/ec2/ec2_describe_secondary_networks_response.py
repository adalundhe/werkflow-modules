from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_secondary_network import EC2SecondaryNetwork


class EC2DescribeSecondaryNetworksResponse(BaseModel):
    SecondaryNetworks: list[EC2SecondaryNetwork] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
