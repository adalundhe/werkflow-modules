from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDetachUserPolicyRequest(BaseModel):
    UserName: StrictStr
    PolicyArn: StrictStr
