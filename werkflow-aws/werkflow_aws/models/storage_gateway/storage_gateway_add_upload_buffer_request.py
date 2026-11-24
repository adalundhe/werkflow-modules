from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayAddUploadBufferRequest(BaseModel):
    GatewayARN: StrictStr
    DiskIds: list[StrictStr]
