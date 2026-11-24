from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateUserRequest(BaseModel):
    UserName: StrictStr
    NewPath: StrictStr | None = None
    NewUserName: StrictStr | None = None
