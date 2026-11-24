from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsDeleteIdentitySourceRequest(BaseModel):
    policyStoreId: StrictStr
    identitySourceId: StrictStr
