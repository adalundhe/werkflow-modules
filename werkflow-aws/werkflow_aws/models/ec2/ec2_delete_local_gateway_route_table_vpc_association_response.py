from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_route_table_vpc_association import EC2LocalGatewayRouteTableVpcAssociation


class EC2DeleteLocalGatewayRouteTableVpcAssociationResponse(BaseModel):
    LocalGatewayRouteTableVpcAssociation: EC2LocalGatewayRouteTableVpcAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
