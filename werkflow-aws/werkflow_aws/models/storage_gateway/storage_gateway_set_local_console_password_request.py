from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewaySetLocalConsolePasswordRequest(BaseModel):
    GatewayARN: StrictStr
    LocalConsolePassword: StrictStr
