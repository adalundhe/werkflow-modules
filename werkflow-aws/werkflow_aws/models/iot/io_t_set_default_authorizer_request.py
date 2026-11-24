from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSetDefaultAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
