from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagPolicyRequest(BaseModel):
    PolicyArn: StrictStr
    TagKeys: list[StrictStr]
