from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2PutPermissionPolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
