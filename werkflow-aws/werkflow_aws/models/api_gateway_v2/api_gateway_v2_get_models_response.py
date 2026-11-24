from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_model import APIGatewayV2Model


class APIGatewayV2GetModelsResponse(BaseModel):
    Items: list[APIGatewayV2Model] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
