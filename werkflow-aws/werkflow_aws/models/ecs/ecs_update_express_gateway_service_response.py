from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_updated_express_gateway_service import ECSUpdatedExpressGatewayService


class ECSUpdateExpressGatewayServiceResponse(BaseModel):
    service: ECSUpdatedExpressGatewayService | None = None
    ResponseMetadata: dict[str, Any] | None = None
