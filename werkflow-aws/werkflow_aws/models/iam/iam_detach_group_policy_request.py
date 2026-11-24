from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDetachGroupPolicyRequest(BaseModel):
    GroupName: StrictStr
    PolicyArn: StrictStr
