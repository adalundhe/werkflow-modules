from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_transit_gateway_prefix_list_attachment import EC2TransitGatewayPrefixListAttachment


class EC2TransitGatewayPrefixListReference(BaseModel):
    TransitGatewayRouteTableId: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    PrefixListOwnerId: StrictStr | None = None
    State: StrictStr | None = None
    Blackhole: StrictBool | None = None
    TransitGatewayAttachment: EC2TransitGatewayPrefixListAttachment | None = None
