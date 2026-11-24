from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_gateway_route import ECSGatewayRoute


class ECSDescribeGatewayRouteResponse(BaseModel):
    gatewayRoute: ECSGatewayRoute | None = None
    ResponseMetadata: dict[str, Any] | None = None
