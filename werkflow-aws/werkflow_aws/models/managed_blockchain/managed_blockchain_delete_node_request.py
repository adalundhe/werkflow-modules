from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainDeleteNodeRequest(BaseModel):
    NetworkId: StrictStr
    NodeId: StrictStr
    MemberId: StrictStr | None = None
