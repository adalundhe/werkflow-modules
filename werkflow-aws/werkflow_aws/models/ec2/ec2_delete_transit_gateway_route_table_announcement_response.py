from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_route_table_announcement import EC2TransitGatewayRouteTableAnnouncement


class EC2DeleteTransitGatewayRouteTableAnnouncementResponse(BaseModel):
    TransitGatewayRouteTableAnnouncement: EC2TransitGatewayRouteTableAnnouncement | None = None
    ResponseMetadata: dict[str, Any] | None = None
