from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutGroupPolicyRequest(BaseModel):
    GroupName: StrictStr
    PolicyName: StrictStr
    PolicyDocument: StrictStr
