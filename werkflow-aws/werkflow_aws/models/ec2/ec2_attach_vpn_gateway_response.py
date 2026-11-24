from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_attachment import EC2VpcAttachment


class EC2AttachVpnGatewayResponse(BaseModel):
    VpcAttachment: EC2VpcAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
