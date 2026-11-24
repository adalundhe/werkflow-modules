from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetSchemaRequest(BaseModel):
    policyStoreId: StrictStr
