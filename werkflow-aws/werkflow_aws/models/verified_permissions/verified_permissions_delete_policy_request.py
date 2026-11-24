from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsDeletePolicyRequest(BaseModel):
    policyStoreId: StrictStr
    policyId: StrictStr
