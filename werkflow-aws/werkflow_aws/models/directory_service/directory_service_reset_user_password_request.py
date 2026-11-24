from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceResetUserPasswordRequest(BaseModel):
    DirectoryId: StrictStr
    UserName: StrictStr
    NewPassword: StrictStr
