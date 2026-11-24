from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .identity_store_group_membership import IdentityStoreGroupMembership


class IdentityStoreListGroupMembershipsForMemberResponse(BaseModel):
    GroupMemberships: list[IdentityStoreGroupMembership] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
