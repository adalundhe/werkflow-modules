from __future__ import annotations
from pydantic import BaseModel
from .ecs_gateway_elb_access_log_s3_destination import ECSGatewayElbAccessLogS3Destination


class ECSGatewayElbAccessLogDestination(BaseModel):
    s3: ECSGatewayElbAccessLogS3Destination | None = None
