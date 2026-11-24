from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsStaticPolicyDefinitionDetail(BaseModel):
    description: StrictStr | None = None
    statement: StrictStr | None = None
