from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_local_gateway_virtual_interface import EC2LocalGatewayVirtualInterface


class EC2DescribeLocalGatewayVirtualInterfacesResponse(BaseModel):
    LocalGatewayVirtualInterfaces: list[EC2LocalGatewayVirtualInterface] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
