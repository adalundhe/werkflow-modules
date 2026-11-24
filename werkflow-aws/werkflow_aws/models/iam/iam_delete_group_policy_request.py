from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteGroupPolicyRequest(BaseModel):
    GroupName: StrictStr
    PolicyName: StrictStr
