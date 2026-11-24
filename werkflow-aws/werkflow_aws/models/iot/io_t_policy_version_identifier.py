from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTPolicyVersionIdentifier(BaseModel):
    policyName: StrictStr | None = None
    policyVersionId: StrictStr | None = None
