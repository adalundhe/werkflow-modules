from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_model import APIGatewayModel


class APIGatewayGetModelsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
