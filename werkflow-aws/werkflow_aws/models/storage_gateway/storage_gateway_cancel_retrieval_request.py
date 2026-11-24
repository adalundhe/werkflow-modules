from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayCancelRetrievalRequest(BaseModel):
    GatewayARN: StrictStr
    TapeARN: StrictStr
