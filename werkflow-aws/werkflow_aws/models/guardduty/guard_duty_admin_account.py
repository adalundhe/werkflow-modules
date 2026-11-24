from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAdminAccount(BaseModel):
    AdminAccountId: StrictStr | None = None
    AdminStatus: StrictStr | None = None
