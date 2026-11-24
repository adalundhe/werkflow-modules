from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainDeleteMemberRequest(BaseModel):
    NetworkId: StrictStr
    MemberId: StrictStr
