from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_request_validator import APIGatewayRequestValidator


class APIGatewayGetRequestValidatorsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayRequestValidator] | None = None
    ResponseMetadata: dict[str, Any] | None = None
