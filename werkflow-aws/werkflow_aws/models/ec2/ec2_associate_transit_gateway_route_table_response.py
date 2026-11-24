from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_association import EC2TransitGatewayAssociation


class EC2AssociateTransitGatewayRouteTableResponse(BaseModel):
    Association: EC2TransitGatewayAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
