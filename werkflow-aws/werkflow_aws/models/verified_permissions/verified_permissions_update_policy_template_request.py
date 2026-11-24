from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdatePolicyTemplateRequest(BaseModel):
    policyStoreId: StrictStr
    policyTemplateId: StrictStr
    statement: StrictStr
    description: StrictStr | None = None
    name: StrictStr | None = None
