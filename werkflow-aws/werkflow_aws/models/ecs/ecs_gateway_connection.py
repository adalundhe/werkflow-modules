from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_connection_resources import ECSGatewayConnectionResources


class ECSGatewayConnection(BaseModel):
    gatewayArn: StrictStr | None = None
    gatewayRouteArn: StrictStr | None = None
    portName: StrictStr | None = None
    serviceUrl: StrictStr | None = None
    accessType: StrictStr | None = None
    status: StrictStr | None = None
    resources: ECSGatewayConnectionResources | None = None
