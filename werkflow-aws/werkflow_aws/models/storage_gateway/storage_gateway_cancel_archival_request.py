from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayCancelArchivalRequest(BaseModel):
    GatewayARN: StrictStr
    TapeARN: StrictStr
