from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubTarget(BaseModel):
    AccountId: StrictStr | None = None
    OrganizationalUnitId: StrictStr | None = None
    RootId: StrictStr | None = None
