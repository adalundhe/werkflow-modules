from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPolicyRole(BaseModel):
    RoleName: StrictStr | None = None
    RoleId: StrictStr | None = None
