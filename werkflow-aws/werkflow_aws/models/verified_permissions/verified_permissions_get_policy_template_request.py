from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetPolicyTemplateRequest(BaseModel):
    policyStoreId: StrictStr
    policyTemplateId: StrictStr
