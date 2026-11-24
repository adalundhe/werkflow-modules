from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_transit_gateway_route import EC2TransitGatewayRoute


class EC2SearchTransitGatewayRoutesResponse(BaseModel):
    Routes: list[EC2TransitGatewayRoute] | None = None
    AdditionalRoutesAvailable: StrictBool | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
