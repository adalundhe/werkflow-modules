from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IAMUpdateRoleRequest(BaseModel):
    RoleName: StrictStr
    Description: StrictStr | None = None
    MaxSessionDuration: StrictInt | None = None
    MaxSigninSessionDuration: StrictInt | None = None
    ResetMaxSigninSessionDuration: StrictBool | None = None
