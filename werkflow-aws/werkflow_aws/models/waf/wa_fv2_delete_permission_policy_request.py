from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2DeletePermissionPolicyRequest(BaseModel):
    ResourceArn: StrictStr
