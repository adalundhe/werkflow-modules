from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAccountDetail(BaseModel):
    accountId: StrictStr
    email: StrictStr
