from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsBatchGetPolicyInputItem(BaseModel):
    policyStoreId: StrictStr
    policyId: StrictStr
