from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCreateResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
    policy: StrictStr
