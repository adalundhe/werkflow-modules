from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_prefix_list_reference import EC2TransitGatewayPrefixListReference


class EC2CreateTransitGatewayPrefixListReferenceResponse(BaseModel):
    TransitGatewayPrefixListReference: EC2TransitGatewayPrefixListReference | None = None
    ResponseMetadata: dict[str, Any] | None = None
