from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_rest_api import APIGatewayRestApi


class APIGatewayGetRestApisResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayRestApi] | None = None
    ResponseMetadata: dict[str, Any] | None = None
