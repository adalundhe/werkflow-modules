from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_definition import VerifiedPermissionsPolicyDefinition


class VerifiedPermissionsCreatePolicyRequest(BaseModel):
    policyStoreId: StrictStr
    definition: VerifiedPermissionsPolicyDefinition
    clientToken: StrictStr | None = None
    name: StrictStr | None = None
