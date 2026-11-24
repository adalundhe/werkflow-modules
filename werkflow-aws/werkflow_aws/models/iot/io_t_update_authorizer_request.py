from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class IoTUpdateAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
    authorizerFunctionArn: StrictStr | None = None
    tokenKeyName: StrictStr | None = None
    tokenSigningPublicKeys: dict[StrictStr, StrictStr] | None = None
    status: Literal['ACTIVE', 'INACTIVE'] | None = None
    enableCachingForHttp: StrictBool | None = None
