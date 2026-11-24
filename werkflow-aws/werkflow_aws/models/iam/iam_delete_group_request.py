from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteGroupRequest(BaseModel):
    GroupName: StrictStr
