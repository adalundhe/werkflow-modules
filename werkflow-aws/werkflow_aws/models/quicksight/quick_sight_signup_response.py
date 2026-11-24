from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightSignupResponse(BaseModel):
    IAMUser: StrictBool | None = None
    userLoginName: StrictStr | None = None
    accountName: StrictStr | None = None
    directoryType: StrictStr | None = None
