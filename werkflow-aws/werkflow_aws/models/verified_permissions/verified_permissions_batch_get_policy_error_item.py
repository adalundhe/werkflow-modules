from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsBatchGetPolicyErrorItem(BaseModel):
    code: StrictStr | None = None
    policyStoreId: StrictStr | None = None
    policyId: StrictStr | None = None
    message: StrictStr | None = None
