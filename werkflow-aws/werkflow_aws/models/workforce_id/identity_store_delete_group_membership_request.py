from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDeleteGroupMembershipRequest(BaseModel):
    IdentityStoreId: StrictStr
    MembershipId: StrictStr
