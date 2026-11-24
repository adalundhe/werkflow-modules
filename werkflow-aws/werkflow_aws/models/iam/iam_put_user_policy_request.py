from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutUserPolicyRequest(BaseModel):
    UserName: StrictStr
    PolicyName: StrictStr
    PolicyDocument: StrictStr
