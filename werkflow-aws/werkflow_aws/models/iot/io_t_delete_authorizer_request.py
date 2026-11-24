from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
