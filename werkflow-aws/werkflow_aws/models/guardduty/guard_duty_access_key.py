from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAccessKey(BaseModel):
    PrincipalId: StrictStr | None = None
    UserName: StrictStr | None = None
    UserType: StrictStr | None = None
