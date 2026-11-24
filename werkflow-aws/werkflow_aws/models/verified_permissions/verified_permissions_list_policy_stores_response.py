from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_store_item import VerifiedPermissionsPolicyStoreItem


class VerifiedPermissionsListPolicyStoresResponse(BaseModel):
    nextToken: StrictStr | None = None
    policyStores: list[VerifiedPermissionsPolicyStoreItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
