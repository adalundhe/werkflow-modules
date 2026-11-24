from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteServiceLinkedRoleRequest(BaseModel):
    RoleName: StrictStr
