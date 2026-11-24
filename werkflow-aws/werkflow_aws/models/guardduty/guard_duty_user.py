from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_account import GuardDutyAccount


class GuardDutyUser(BaseModel):
    Name: StrictStr | None = None
    Uid: StrictStr | None = None
    Type: StrictStr | None = None
    CredentialUid: StrictStr | None = None
    Account: GuardDutyAccount | None = None
