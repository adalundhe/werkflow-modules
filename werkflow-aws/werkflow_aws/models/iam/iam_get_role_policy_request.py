from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetRolePolicyRequest(BaseModel):
    RoleName: StrictStr
    PolicyName: StrictStr
