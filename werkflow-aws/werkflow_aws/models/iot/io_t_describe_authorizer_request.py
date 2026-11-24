from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeAuthorizerRequest(BaseModel):
    authorizerName: StrictStr
