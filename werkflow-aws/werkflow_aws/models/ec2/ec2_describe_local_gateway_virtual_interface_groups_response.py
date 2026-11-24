from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_local_gateway_virtual_interface_group import EC2LocalGatewayVirtualInterfaceGroup


class EC2DescribeLocalGatewayVirtualInterfaceGroupsResponse(BaseModel):
    LocalGatewayVirtualInterfaceGroups: list[EC2LocalGatewayVirtualInterfaceGroup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
