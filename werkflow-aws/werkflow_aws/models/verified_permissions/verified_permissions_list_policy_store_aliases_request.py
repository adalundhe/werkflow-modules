from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .verified_permissions_policy_store_alias_filter import VerifiedPermissionsPolicyStoreAliasFilter


class VerifiedPermissionsListPolicyStoreAliasesRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: VerifiedPermissionsPolicyStoreAliasFilter | None = None
