from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayRetrieveTapeRecoveryPointRequest(BaseModel):
    TapeARN: StrictStr
    GatewayARN: StrictStr
