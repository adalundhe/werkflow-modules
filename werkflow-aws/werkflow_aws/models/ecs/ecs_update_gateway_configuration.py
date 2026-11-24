from __future__ import annotations
from pydantic import BaseModel
from .ecs_update_gateway_alb_configuration import ECSUpdateGatewayAlbConfiguration


class ECSUpdateGatewayConfiguration(BaseModel):
    hostSharedAlb: ECSUpdateGatewayAlbConfiguration | None = None
