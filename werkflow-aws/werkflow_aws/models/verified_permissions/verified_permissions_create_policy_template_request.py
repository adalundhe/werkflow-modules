from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCreatePolicyTemplateRequest(BaseModel):
    policyStoreId: StrictStr
    statement: StrictStr
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None
