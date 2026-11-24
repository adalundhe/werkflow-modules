from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsIdentitySourceFilter(BaseModel):
    principalEntityType: StrictStr | None = None
