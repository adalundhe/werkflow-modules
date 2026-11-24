from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class VerifiedPermissionsListPolicyTemplatesRequest(BaseModel):
    policyStoreId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
