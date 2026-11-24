from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_vpc_attachment import EC2TransitGatewayVpcAttachment


class EC2ModifyTransitGatewayVpcAttachmentResponse(BaseModel):
    TransitGatewayVpcAttachment: EC2TransitGatewayVpcAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
