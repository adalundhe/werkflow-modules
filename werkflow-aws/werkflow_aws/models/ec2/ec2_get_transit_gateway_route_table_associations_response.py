from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_route_table_association import EC2TransitGatewayRouteTableAssociation


class EC2GetTransitGatewayRouteTableAssociationsResponse(BaseModel):
    Associations: list[EC2TransitGatewayRouteTableAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
