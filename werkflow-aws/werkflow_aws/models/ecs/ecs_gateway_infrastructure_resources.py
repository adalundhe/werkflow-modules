from __future__ import annotations
from pydantic import BaseModel
from .ecs_elb_gateway_resources import ECSElbGatewayResources


class ECSGatewayInfrastructureResources(BaseModel):
    hostSharedAlb: list[ECSElbGatewayResources] | None = None
