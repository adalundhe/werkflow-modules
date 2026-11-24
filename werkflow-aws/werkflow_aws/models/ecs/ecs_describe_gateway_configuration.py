from __future__ import annotations
from pydantic import BaseModel
from .ecs_describe_gateway_alb_configuration import ECSDescribeGatewayAlbConfiguration


class ECSDescribeGatewayConfiguration(BaseModel):
    hostSharedAlb: ECSDescribeGatewayAlbConfiguration | None = None
