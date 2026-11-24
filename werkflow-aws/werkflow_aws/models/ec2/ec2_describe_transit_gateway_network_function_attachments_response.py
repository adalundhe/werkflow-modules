from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_network_function_attachment import EC2TransitGatewayNetworkFunctionAttachment


class EC2DescribeTransitGatewayNetworkFunctionAttachmentsResponse(BaseModel):
    TransitGatewayNetworkFunctionAttachments: list[EC2TransitGatewayNetworkFunctionAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
