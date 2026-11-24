from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCreatePolicyStoreAliasRequest(BaseModel):
    aliasName: StrictStr
    policyStoreId: StrictStr
