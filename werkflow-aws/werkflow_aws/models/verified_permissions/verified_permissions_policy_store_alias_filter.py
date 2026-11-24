from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsPolicyStoreAliasFilter(BaseModel):
    policyStoreId: StrictStr | None = None
