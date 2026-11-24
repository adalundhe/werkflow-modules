from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutRolePermissionsBoundaryRequest(BaseModel):
    RoleName: StrictStr
    PermissionsBoundary: StrictStr
