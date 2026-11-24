from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetUserRequest(BaseModel):
    UserName: StrictStr | None = None
