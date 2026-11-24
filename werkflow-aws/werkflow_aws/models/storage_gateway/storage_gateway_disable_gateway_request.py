from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDisableGatewayRequest(BaseModel):
    GatewayARN: StrictStr
