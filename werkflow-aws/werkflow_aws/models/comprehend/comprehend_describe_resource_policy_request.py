from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
