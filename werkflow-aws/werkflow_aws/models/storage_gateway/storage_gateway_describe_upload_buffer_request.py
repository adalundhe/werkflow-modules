from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeUploadBufferRequest(BaseModel):
    GatewayARN: StrictStr
