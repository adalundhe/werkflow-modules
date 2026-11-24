from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_attachment import EC2TransitGatewayAttachment


class EC2DescribeTransitGatewayAttachmentsResponse(BaseModel):
    TransitGatewayAttachments: list[EC2TransitGatewayAttachment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
