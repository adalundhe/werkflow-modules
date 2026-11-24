from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_gateway import ECSGateway


class ECSDescribeGatewayResponse(BaseModel):
    gateway: ECSGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None
