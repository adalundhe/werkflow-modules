from __future__ import annotations
from pydantic import BaseModel
from .ecs_host_shared_alb_configuration import ECSHostSharedAlbConfiguration


class ECSGatewayConfiguration(BaseModel):
    hostSharedAlb: ECSHostSharedAlbConfiguration | None = None
