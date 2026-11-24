from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_gateway_resources import ECSGatewayResources


class ECSDescribeGatewayResourcesResponse(BaseModel):
    gatewayResources: ECSGatewayResources | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
