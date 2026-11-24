from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeWorkingStorageRequest(BaseModel):
    GatewayARN: StrictStr
