from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAttachGroupPolicyRequest(BaseModel):
    GroupName: StrictStr
    PolicyArn: StrictStr
