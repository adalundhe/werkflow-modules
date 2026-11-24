from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_virtual_interface_group import EC2LocalGatewayVirtualInterfaceGroup


class EC2CreateLocalGatewayVirtualInterfaceGroupResponse(BaseModel):
    LocalGatewayVirtualInterfaceGroup: EC2LocalGatewayVirtualInterfaceGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
