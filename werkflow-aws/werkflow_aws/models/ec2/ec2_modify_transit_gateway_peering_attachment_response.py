from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_peering_attachment import EC2TransitGatewayPeeringAttachment


class EC2ModifyTransitGatewayPeeringAttachmentResponse(BaseModel):
    TransitGatewayPeeringAttachment: EC2TransitGatewayPeeringAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
