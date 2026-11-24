from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class VerifiedPermissionsGetPolicyStoreRequest(BaseModel):
    policyStoreId: StrictStr
    tags: StrictBool | None = None
