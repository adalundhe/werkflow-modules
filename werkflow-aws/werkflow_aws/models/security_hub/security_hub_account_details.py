from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAccountDetails(BaseModel):
    AccountId: StrictStr
    Email: StrictStr | None = None
