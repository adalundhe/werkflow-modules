from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_gateway_route_summary import ECSGatewayRouteSummary


class ECSListGatewayRoutesResponse(BaseModel):
    gatewayRoutes: list[ECSGatewayRouteSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
