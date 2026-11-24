from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationUpdateRLSPolicyRequest(BaseModel):
    Name: StrictStr
    FilterExpression: StrictStr | None = None
