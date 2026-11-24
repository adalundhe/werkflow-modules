from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateAssumeRolePolicyRequest(BaseModel):
    RoleName: StrictStr
    PolicyDocument: StrictStr
