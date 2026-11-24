from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_route_response import APIGatewayV2RouteResponse


class APIGatewayV2GetRouteResponsesResponse(BaseModel):
    Items: list[APIGatewayV2RouteResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
