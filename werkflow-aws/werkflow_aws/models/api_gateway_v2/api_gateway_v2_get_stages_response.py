from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_stage import APIGatewayV2Stage


class APIGatewayV2GetStagesResponse(BaseModel):
    Items: list[APIGatewayV2Stage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
