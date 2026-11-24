from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetPolicyRequest(BaseModel):
    PolicyArn: StrictStr
