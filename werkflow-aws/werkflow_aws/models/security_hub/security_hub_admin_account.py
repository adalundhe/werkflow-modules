from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAdminAccount(BaseModel):
    AccountId: StrictStr | None = None
    Status: StrictStr | None = None
