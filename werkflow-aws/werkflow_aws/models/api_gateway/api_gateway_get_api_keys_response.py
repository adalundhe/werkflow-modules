from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_api_key import APIGatewayApiKey


class APIGatewayGetApiKeysResponse(BaseModel):
    warnings: list[StrictStr] | None = None
    position: StrictStr | None = None
    items: list[APIGatewayApiKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
