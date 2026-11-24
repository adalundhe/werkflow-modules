from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_gateway_infrastructure_resources import ECSGatewayInfrastructureResources


class ECSGatewayResources(BaseModel):
    gatewayArn: StrictStr | None = None
    resources: ECSGatewayInfrastructureResources | None = None
