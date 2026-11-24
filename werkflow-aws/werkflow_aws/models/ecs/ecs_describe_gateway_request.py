from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDescribeGatewayRequest(BaseModel):
    gateway: StrictStr
