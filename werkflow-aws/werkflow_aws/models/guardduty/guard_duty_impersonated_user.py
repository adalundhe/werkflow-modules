from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyImpersonatedUser(BaseModel):
    Username: StrictStr | None = None
    Groups: list[StrictStr] | None = None
