from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .identity_store_member_id import IdentityStoreMemberId


class IdentityStoreIsMemberInGroupsRequest(BaseModel):
    IdentityStoreId: StrictStr
    MemberId: IdentityStoreMemberId
    GroupIds: list[StrictStr]
