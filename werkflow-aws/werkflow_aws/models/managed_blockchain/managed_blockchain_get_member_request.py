from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainGetMemberRequest(BaseModel):
    NetworkId: StrictStr
    MemberId: StrictStr
