from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveAccount(BaseModel):
    AccountId: StrictStr
    EmailAddress: StrictStr
