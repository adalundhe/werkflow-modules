from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayAddWorkingStorageRequest(BaseModel):
    GatewayARN: StrictStr
    DiskIds: list[StrictStr]
