from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_route_alb_resources import ECSGatewayRouteAlbResources


class ECSGatewayRouteResources(BaseModel):
    hostSharedAlb: list[ECSGatewayRouteAlbResources] | None = None
