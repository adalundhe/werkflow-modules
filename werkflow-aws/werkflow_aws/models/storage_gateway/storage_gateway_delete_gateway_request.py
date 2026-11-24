from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteGatewayRequest(BaseModel):
    GatewayARN: StrictStr
