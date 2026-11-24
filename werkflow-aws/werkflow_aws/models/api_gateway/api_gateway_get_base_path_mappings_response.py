from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_base_path_mapping import APIGatewayBasePathMapping


class APIGatewayGetBasePathMappingsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayBasePathMapping] | None = None
    ResponseMetadata: dict[str, Any] | None = None
