from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IAMCreateLoginProfileRequest(BaseModel):
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
    PasswordResetRequired: StrictBool | None = None
    MaxSigninSessionDuration: StrictInt | None = None
