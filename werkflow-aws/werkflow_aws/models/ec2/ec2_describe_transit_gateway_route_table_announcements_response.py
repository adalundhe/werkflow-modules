from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_route_table_announcement import EC2TransitGatewayRouteTableAnnouncement


class EC2DescribeTransitGatewayRouteTableAnnouncementsResponse(BaseModel):
    TransitGatewayRouteTableAnnouncements: list[EC2TransitGatewayRouteTableAnnouncement] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
