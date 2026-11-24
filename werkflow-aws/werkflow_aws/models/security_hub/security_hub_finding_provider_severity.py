from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubFindingProviderSeverity(BaseModel):
    Label: StrictStr | None = None
    Original: StrictStr | None = None
