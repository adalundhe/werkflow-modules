from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_route_resources import ECSGatewayRouteResources


class ECSGatewayRoute(BaseModel):
    gatewayRouteArn: StrictStr | None = None
    serviceArn: StrictStr | None = None
    serviceContainerPortName: StrictStr | None = None
    status: StrictStr | None = None
    serviceUrl: StrictStr | None = None
    resources: ECSGatewayRouteResources | None = None
