from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeCacheRequest(BaseModel):
    GatewayARN: StrictStr
