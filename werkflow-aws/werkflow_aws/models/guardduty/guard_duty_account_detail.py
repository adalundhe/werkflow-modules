from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAccountDetail(BaseModel):
    AccountId: StrictStr
    Email: StrictStr
