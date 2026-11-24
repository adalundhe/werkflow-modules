from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_update_gateway_configuration import ECSUpdateGatewayConfiguration


class ECSUpdateGatewayRequest(BaseModel):
    gateway: StrictStr
    infrastructureRoleArn: StrictStr | None = None
    deletionProtection: StrictBool | None = None
    configuration: ECSUpdateGatewayConfiguration | None = None
    propagateTags: Literal['NONE', 'GATEWAY'] | None = None
