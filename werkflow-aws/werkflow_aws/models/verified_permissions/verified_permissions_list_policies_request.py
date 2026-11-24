from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .verified_permissions_policy_filter import VerifiedPermissionsPolicyFilter


class VerifiedPermissionsListPoliciesRequest(BaseModel):
    policyStoreId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filter: VerifiedPermissionsPolicyFilter | None = None
