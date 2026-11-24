from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_api import APIGatewayV2Api


class APIGatewayV2GetApisResponse(BaseModel):
    Items: list[APIGatewayV2Api] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
