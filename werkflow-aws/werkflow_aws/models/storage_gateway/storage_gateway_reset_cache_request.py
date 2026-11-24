from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayResetCacheRequest(BaseModel):
    GatewayARN: StrictStr
