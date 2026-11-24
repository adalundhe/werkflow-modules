from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeResourcePolicyRequest(BaseModel):
    resourceArn: StrictStr
