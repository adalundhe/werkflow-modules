from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayAssignTapePoolRequest(BaseModel):
    TapeARN: StrictStr
    PoolId: StrictStr
    BypassGovernanceRetention: StrictBool | None = None
