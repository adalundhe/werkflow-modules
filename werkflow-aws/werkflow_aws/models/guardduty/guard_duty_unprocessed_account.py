from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyUnprocessedAccount(BaseModel):
    AccountId: StrictStr | None = None
    Result: StrictStr | None = None
