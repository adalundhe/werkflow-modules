from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMRemoveRoleFromInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
    RoleName: StrictStr
