from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_elb_access_log_destination import ECSGatewayElbAccessLogDestination


class ECSGatewayElbAccessLogConfiguration(BaseModel):
    destination: ECSGatewayElbAccessLogDestination | None = None
