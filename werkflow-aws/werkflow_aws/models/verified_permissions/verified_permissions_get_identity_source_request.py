from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetIdentitySourceRequest(BaseModel):
    policyStoreId: StrictStr
    identitySourceId: StrictStr
