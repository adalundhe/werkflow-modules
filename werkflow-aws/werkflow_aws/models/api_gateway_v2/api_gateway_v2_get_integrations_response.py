from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_integration import APIGatewayV2Integration


class APIGatewayV2GetIntegrationsResponse(BaseModel):
    Items: list[APIGatewayV2Integration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
