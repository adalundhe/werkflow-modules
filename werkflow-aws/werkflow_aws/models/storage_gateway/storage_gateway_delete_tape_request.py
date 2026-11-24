from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayDeleteTapeRequest(BaseModel):
    GatewayARN: StrictStr
    TapeARN: StrictStr
    BypassGovernanceRetention: StrictBool | None = None
