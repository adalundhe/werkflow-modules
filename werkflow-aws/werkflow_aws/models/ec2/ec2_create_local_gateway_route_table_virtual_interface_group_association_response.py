from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_route_table_virtual_interface_group_association import EC2LocalGatewayRouteTableVirtualInterfaceGroupAssociation


class EC2CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResponse(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: EC2LocalGatewayRouteTableVirtualInterfaceGroupAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
