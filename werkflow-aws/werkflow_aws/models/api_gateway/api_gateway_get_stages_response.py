from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .api_gateway_stage import APIGatewayStage


class APIGatewayGetStagesResponse(BaseModel):
    item: list[APIGatewayStage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
