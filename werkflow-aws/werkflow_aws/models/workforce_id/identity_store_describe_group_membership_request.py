from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreDescribeGroupMembershipRequest(BaseModel):
    IdentityStoreId: StrictStr
    MembershipId: StrictStr
