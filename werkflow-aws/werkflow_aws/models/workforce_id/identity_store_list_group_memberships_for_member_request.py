from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .identity_store_member_id import IdentityStoreMemberId


class IdentityStoreListGroupMembershipsForMemberRequest(BaseModel):
    IdentityStoreId: StrictStr
    MemberId: IdentityStoreMemberId
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
