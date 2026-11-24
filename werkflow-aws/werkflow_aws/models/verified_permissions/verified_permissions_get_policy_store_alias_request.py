from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetPolicyStoreAliasRequest(BaseModel):
    aliasName: StrictStr
