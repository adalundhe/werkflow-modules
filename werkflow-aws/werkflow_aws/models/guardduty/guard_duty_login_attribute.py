from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyLoginAttribute(BaseModel):
    User: StrictStr | None = None
    Application: StrictStr | None = None
    FailedLoginAttempts: StrictInt | None = None
    SuccessfulLoginAttempts: StrictInt | None = None
