from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsDeterminingPolicyItem(BaseModel):
    policyId: StrictStr | None = None
