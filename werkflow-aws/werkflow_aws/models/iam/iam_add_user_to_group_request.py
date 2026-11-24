from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAddUserToGroupRequest(BaseModel):
    GroupName: StrictStr
    UserName: StrictStr
