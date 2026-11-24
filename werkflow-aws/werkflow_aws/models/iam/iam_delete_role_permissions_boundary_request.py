from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteRolePermissionsBoundaryRequest(BaseModel):
    RoleName: StrictStr
