from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetGroupPolicyRequest(BaseModel):
    GroupName: StrictStr
    PolicyName: StrictStr
