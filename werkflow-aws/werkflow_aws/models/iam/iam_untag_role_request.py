from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagRoleRequest(BaseModel):
    RoleName: StrictStr
    TagKeys: list[StrictStr]
