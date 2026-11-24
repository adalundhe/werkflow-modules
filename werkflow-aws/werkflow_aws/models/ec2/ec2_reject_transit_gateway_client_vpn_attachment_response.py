from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_client_vpn_attachment import EC2TransitGatewayClientVpnAttachment


class EC2RejectTransitGatewayClientVpnAttachmentResponse(BaseModel):
    TransitGatewayClientVpnAttachment: EC2TransitGatewayClientVpnAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
