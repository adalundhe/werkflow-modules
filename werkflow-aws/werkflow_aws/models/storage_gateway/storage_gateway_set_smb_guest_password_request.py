from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewaySetSMBGuestPasswordRequest(BaseModel):
    GatewayARN: StrictStr
    Password: StrictStr
