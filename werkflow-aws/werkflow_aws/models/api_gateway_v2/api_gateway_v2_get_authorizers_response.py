from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_authorizer import APIGatewayV2Authorizer


class APIGatewayV2GetAuthorizersResponse(BaseModel):
    Items: list[APIGatewayV2Authorizer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
