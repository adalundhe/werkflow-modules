from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainGetNetworkRequest(BaseModel):
    NetworkId: StrictStr
