from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_express_gateway_service import ECSExpressGatewayService


class ECSDeleteExpressGatewayServiceResponse(BaseModel):
    service: ECSExpressGatewayService | None = None
    ResponseMetadata: dict[str, Any] | None = None
