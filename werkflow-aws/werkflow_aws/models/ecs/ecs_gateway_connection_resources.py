from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_connection_alb_resources import ECSGatewayConnectionAlbResources


class ECSGatewayConnectionResources(BaseModel):
    hostSharedAlb: list[ECSGatewayConnectionAlbResources] | None = None
