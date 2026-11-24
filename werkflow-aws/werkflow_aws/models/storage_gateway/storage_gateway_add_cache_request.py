from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayAddCacheRequest(BaseModel):
    GatewayARN: StrictStr
    DiskIds: list[StrictStr]
