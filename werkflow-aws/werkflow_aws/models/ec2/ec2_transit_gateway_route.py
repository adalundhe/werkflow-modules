from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_route_attachment import EC2TransitGatewayRouteAttachment


class EC2TransitGatewayRoute(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    TransitGatewayRouteTableAnnouncementId: StrictStr | None = None
    TransitGatewayAttachments: list[EC2TransitGatewayRouteAttachment] | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
