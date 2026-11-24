from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteTapePoolRequest(BaseModel):
    PoolARN: StrictStr
