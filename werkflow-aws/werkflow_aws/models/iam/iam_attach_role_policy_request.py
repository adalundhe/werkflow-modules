from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAttachRolePolicyRequest(BaseModel):
    RoleName: StrictStr
    PolicyArn: StrictStr
