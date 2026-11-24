from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_store_alias_item import VerifiedPermissionsPolicyStoreAliasItem


class VerifiedPermissionsListPolicyStoreAliasesResponse(BaseModel):
    nextToken: StrictStr | None = None
    policyStoreAliases: list[VerifiedPermissionsPolicyStoreAliasItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
