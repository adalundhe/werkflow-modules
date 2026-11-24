from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
