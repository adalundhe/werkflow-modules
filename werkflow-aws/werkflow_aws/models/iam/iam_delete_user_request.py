from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteUserRequest(BaseModel):
    UserName: StrictStr
