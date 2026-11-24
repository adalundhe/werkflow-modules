from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayDeleteTapeArchiveRequest(BaseModel):
    TapeARN: StrictStr
    BypassGovernanceRetention: StrictBool | None = None
