from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_prefix_list_reference import EC2TransitGatewayPrefixListReference


class EC2GetTransitGatewayPrefixListReferencesResponse(BaseModel):
    TransitGatewayPrefixListReferences: list[EC2TransitGatewayPrefixListReference] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
