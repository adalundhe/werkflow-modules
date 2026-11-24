from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_gateway_response import APIGatewayGatewayResponse


class APIGatewayGetGatewayResponsesResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayGatewayResponse] | None = None
    ResponseMetadata: dict[str, Any] | None = None
