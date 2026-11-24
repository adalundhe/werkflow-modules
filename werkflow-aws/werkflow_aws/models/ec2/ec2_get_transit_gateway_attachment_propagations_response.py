from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_attachment_propagation import EC2TransitGatewayAttachmentPropagation


class EC2GetTransitGatewayAttachmentPropagationsResponse(BaseModel):
    TransitGatewayAttachmentPropagations: list[EC2TransitGatewayAttachmentPropagation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
