from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_test_traffic_header import ECSGatewayTestTrafficHeader


class ECSGatewayAlbTestTrafficRules(BaseModel):
    header: ECSGatewayTestTrafficHeader | None = None
