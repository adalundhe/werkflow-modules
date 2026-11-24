from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAddRoleToInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
    RoleName: StrictStr
