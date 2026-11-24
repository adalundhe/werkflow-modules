from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_deployment import APIGatewayV2Deployment


class APIGatewayV2GetDeploymentsResponse(BaseModel):
    Items: list[APIGatewayV2Deployment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
