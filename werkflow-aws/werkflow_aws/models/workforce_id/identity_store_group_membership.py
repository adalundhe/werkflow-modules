from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .identity_store_member_id import IdentityStoreMemberId


class IdentityStoreGroupMembership(BaseModel):
    IdentityStoreId: StrictStr | None = None
    MembershipId: StrictStr | None = None
    MembershipArn: StrictStr | None = None
    GroupId: StrictStr | None = None
    MemberId: IdentityStoreMemberId | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    UpdatedBy: StrictStr | None = None
