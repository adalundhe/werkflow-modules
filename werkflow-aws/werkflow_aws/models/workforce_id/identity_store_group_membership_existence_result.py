from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .identity_store_member_id import IdentityStoreMemberId


class IdentityStoreGroupMembershipExistenceResult(BaseModel):
    GroupId: StrictStr | None = None
    MemberId: IdentityStoreMemberId | None = None
    MembershipExists: StrictBool | None = None
