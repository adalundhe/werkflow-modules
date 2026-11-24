from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IAMLoginProfile(BaseModel):
    UserName: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    PasswordResetRequired: StrictBool | None = None
    MaxSigninSessionDuration: StrictInt | None = None
