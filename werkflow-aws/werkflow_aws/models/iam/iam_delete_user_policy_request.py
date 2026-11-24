from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteUserPolicyRequest(BaseModel):
    UserName: StrictStr
    PolicyName: StrictStr
