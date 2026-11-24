from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_peering_attachment import EC2TransitGatewayPeeringAttachment


class EC2DescribeTransitGatewayPeeringAttachmentsResponse(BaseModel):
    TransitGatewayPeeringAttachments: list[EC2TransitGatewayPeeringAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
