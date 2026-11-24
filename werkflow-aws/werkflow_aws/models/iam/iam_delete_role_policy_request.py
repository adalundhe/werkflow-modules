from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteRolePolicyRequest(BaseModel):
    RoleName: StrictStr
    PolicyName: StrictStr
