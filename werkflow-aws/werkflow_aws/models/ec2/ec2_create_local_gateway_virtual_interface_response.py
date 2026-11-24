from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_virtual_interface import EC2LocalGatewayVirtualInterface


class EC2CreateLocalGatewayVirtualInterfaceResponse(BaseModel):
    LocalGatewayVirtualInterface: EC2LocalGatewayVirtualInterface | None = None
    ResponseMetadata: dict[str, Any] | None = None
