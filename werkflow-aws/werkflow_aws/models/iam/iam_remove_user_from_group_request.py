from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMRemoveUserFromGroupRequest(BaseModel):
    GroupName: StrictStr
    UserName: StrictStr
