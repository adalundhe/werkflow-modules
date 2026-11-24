from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetPolicyRequest(BaseModel):
    policyStoreId: StrictStr
    policyId: StrictStr
