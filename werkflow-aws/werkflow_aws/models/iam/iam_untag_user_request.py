from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagUserRequest(BaseModel):
    UserName: StrictStr
    TagKeys: list[StrictStr]
