from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeleteRLSPolicyRequest(BaseModel):
    Name: StrictStr
