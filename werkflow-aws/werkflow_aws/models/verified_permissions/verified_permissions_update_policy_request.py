from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_update_policy_definition import VerifiedPermissionsUpdatePolicyDefinition


class VerifiedPermissionsUpdatePolicyRequest(BaseModel):
    policyStoreId: StrictStr
    policyId: StrictStr
    definition: VerifiedPermissionsUpdatePolicyDefinition | None = None
    name: StrictStr | None = None
