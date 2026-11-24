from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAzureScopeConfiguration(BaseModel):
    ScopeType: StrictStr | None = None
    ScopeValues: list[StrictStr] | None = None
