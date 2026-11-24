from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .identity_store_group_membership_existence_result import IdentityStoreGroupMembershipExistenceResult


class IdentityStoreIsMemberInGroupsResponse(BaseModel):
    Results: list[IdentityStoreGroupMembershipExistenceResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
