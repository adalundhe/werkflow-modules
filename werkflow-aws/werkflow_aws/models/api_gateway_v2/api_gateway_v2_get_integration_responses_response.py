from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_integration_response import APIGatewayV2IntegrationResponse


class APIGatewayV2GetIntegrationResponsesResponse(BaseModel):
    Items: list[APIGatewayV2IntegrationResponse] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
