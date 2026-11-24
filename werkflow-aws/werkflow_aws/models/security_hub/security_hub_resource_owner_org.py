from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubResourceOwnerOrg(BaseModel):
    Id: StrictStr | None = None
