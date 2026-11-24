from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_gateway_summary import ECSGatewaySummary


class ECSListGatewaysResponse(BaseModel):
    gateways: list[ECSGatewaySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
