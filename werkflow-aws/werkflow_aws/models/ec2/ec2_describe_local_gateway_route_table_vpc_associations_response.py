from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_local_gateway_route_table_vpc_association import EC2LocalGatewayRouteTableVpcAssociation


class EC2DescribeLocalGatewayRouteTableVpcAssociationsResponse(BaseModel):
    LocalGatewayRouteTableVpcAssociations: list[EC2LocalGatewayRouteTableVpcAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
