from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMChangePasswordRequest(BaseModel):
    OldPassword: StrictStr
    NewPassword: StrictStr
