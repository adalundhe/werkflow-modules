from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_gateway_configuration import ECSGatewayConfiguration
from .ecs_tag import ECSTag


class ECSCreateGatewayRequest(BaseModel):
    name: StrictStr
    infrastructureRoleArn: StrictStr
    configuration: ECSGatewayConfiguration
    clientToken: StrictStr | None = None
    deletionProtection: StrictBool | None = None
    tags: list[ECSTag] | None = None
    propagateTags: Literal['NONE', 'GATEWAY'] | None = None
