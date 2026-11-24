from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IAMUpdateLoginProfileRequest(BaseModel):
    UserName: StrictStr
    Password: StrictStr | None = None
    PasswordResetRequired: StrictBool | None = None
    MaxSigninSessionDuration: StrictInt | None = None
    ResetMaxSigninSessionDuration: StrictBool | None = None
