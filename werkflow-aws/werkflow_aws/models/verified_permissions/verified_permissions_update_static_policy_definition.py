from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateStaticPolicyDefinition(BaseModel):
    statement: StrictStr
    description: StrictStr | None = None
