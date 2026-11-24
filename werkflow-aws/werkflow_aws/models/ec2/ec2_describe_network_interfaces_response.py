from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_interface import EC2NetworkInterface


class EC2DescribeNetworkInterfacesResponse(BaseModel):
    NetworkInterfaces: list[EC2NetworkInterface] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
