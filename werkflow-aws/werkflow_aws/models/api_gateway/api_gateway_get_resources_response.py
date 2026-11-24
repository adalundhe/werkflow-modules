from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_resource import APIGatewayResource


class APIGatewayGetResourcesResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
