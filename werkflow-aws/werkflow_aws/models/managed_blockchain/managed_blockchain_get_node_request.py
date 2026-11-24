from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainGetNodeRequest(BaseModel):
    NetworkId: StrictStr
    NodeId: StrictStr
    MemberId: StrictStr | None = None
