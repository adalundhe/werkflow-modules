from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetUserPolicyRequest(BaseModel):
    UserName: StrictStr
    PolicyName: StrictStr
