from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_api_mapping import APIGatewayV2ApiMapping


class APIGatewayV2GetApiMappingsResponse(BaseModel):
    Items: list[APIGatewayV2ApiMapping] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
