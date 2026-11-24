from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteRoleRequest(BaseModel):
    RoleName: StrictStr
