from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway import EC2TransitGateway


class EC2ModifyTransitGatewayResponse(BaseModel):
    TransitGateway: EC2TransitGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None
