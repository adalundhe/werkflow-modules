from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetRoleRequest(BaseModel):
    RoleName: StrictStr
