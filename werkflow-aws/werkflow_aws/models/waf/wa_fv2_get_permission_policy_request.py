from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2GetPermissionPolicyRequest(BaseModel):
    ResourceArn: StrictStr
