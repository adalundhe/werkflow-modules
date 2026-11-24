from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubResourceOwnerAccount(BaseModel):
    Id: StrictStr | None = None
