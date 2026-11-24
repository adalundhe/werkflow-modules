from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayRetrieveTapeArchiveRequest(BaseModel):
    TapeARN: StrictStr
    GatewayARN: StrictStr
