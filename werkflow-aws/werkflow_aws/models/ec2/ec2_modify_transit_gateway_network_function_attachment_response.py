from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_network_function_attachment import EC2TransitGatewayNetworkFunctionAttachment


class EC2ModifyTransitGatewayNetworkFunctionAttachmentResponse(BaseModel):
    TransitGatewayNetworkFunctionAttachment: EC2TransitGatewayNetworkFunctionAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
