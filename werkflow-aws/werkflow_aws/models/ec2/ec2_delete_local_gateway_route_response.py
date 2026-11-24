from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_local_gateway_route import EC2LocalGatewayRoute


class EC2DeleteLocalGatewayRouteResponse(BaseModel):
    Route: EC2LocalGatewayRoute | None = None
    ResponseMetadata: dict[str, Any] | None = None
