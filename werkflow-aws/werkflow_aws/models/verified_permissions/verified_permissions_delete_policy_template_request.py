from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsDeletePolicyTemplateRequest(BaseModel):
    policyStoreId: StrictStr
    policyTemplateId: StrictStr
