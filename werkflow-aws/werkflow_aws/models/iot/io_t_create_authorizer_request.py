from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_tag import IoTTag


class IoTCreateAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
    authorizerFunctionArn: StrictStr
    tokenKeyName: StrictStr | None = None
    tokenSigningPublicKeys: dict[StrictStr, StrictStr] | None = None
    status: Literal['ACTIVE', 'INACTIVE'] | None = None
    tags: list[IoTTag] | None = None
    signingDisabled: StrictBool | None = None
    enableCachingForHttp: StrictBool | None = None
