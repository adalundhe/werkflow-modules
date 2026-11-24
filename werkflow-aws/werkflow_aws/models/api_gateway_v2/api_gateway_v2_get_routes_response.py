from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_route import APIGatewayV2Route


class APIGatewayV2GetRoutesResponse(BaseModel):
    Items: list[APIGatewayV2Route] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
