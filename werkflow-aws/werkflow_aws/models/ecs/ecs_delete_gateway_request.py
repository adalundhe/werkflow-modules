from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteGatewayRequest(BaseModel):
    gateway: StrictStr
