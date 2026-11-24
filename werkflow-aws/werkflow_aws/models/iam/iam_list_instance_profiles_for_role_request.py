from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListInstanceProfilesForRoleRequest(BaseModel):
    RoleName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
