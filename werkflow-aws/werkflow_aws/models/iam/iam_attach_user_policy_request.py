from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAttachUserPolicyRequest(BaseModel):
    UserName: StrictStr
    PolicyArn: StrictStr
