from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutRolePolicyRequest(BaseModel):
    RoleName: StrictStr
    PolicyName: StrictStr
    PolicyDocument: StrictStr
